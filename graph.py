import pygame as pg
from math import inf

class Graph:

    class Node:
        
        def __init__(self,value,x,y):
            self.value = value
            self.x = x
            self.y = y
        
        def draw(self,surface,r):
            font = pg.font.Font(None,20)
            text_surface = font.render((str)(self.value),True,(0,0,0))
            pg.draw.circle(surface,(215,214,227),(self.x,self.y),r)
            surface.blit(text_surface,(self.x-(text_surface.get_width()/2),self.y-(text_surface.get_height()/2)))

    def __init__(self): 
        self.nodes = []
        self.adjacency = [[None]*0 for i in range(0)]

    def is_in_graph(self,wanted):
        for node in self.nodes:
            if node.value == wanted: return True
        return False
    
    def index(self,wanted):
        for i in range(len(self.nodes)):
            if wanted == self.nodes[i].value:
                return i
        return 0


    def insert(self,value,x,y):
        if self.is_in_graph(value): return False

        self.nodes.append(self.Node(value,x,y))
        rows = columns = len(self.adjacency)
        matrix_aux = [[0] * (rows + 1) for i in range(columns + 1)]
        for f in range(rows):
            for c in range(columns):
                matrix_aux[f][c] = self.adjacency[f][c]
        self.adjacency = matrix_aux
        return True

    def add_edge(self,begin,end,weight,directed):
        if not(self.is_in_graph(begin)) and (self.is_in_graph(end)): return False
        self.adjacency[self.index(begin)][self.index(end)] = weight
        if not directed: self.adjacency[self.index(end)][self.index(begin)] = weight
        else: return True
    
    def set_edge_weight(self,begin,end,weight,directed):
        if not(self.is_in_graph(begin) and self.is_in_graph(end)): return False
        if self.adjacency[self.index(begin)][self.index(end)] != 0:
            self.adjacency[self.index(begin)][self.index(end)] = weight
            if not directed: self.adjacency[self.index(end)][self.index(begin)] = weight     

    def clear_edges(self):
        rows = columns = len(self.adjacency)
        for r in range(rows):
            for c in range(columns):
                self.adjacency[r][c] = 0

    def get_succesors(self, value):
        edge_pos = self.index(value)
        list_successors = []
        for i in range(len(self.adjacency)):
            if self.adjacency[edge_pos][i] != 0:
                list_successors.append((self.nodes[i], self.adjacency[edge_pos][i]))

        return list_successors
    
    def dijkstra(self, start, end=-1):
        n = len(self.adjacency)
        dist = [inf]*n
        dist[start] = self.adjacency[start][start]  # 0
        spVertex = [False]*n
        parent = [-1]*n

        path = [{}]*n

        for count in range(n-1):
            minix = inf
            u = 0
            for v in range(len(spVertex)):
                if spVertex[v] == False and dist[v] <= minix:
                    minix = dist[v]
                    u = v
            spVertex[u] = True
            for v in range(n):
                if not(spVertex[v]) and self.adjacency[u][v] != 0 and dist[u] + self.adjacency[u][v] < dist[v]:
                    parent[v] = u
                    dist[v] = dist[u] + self.adjacency[u][v]

        for i in range(n):
            j = i
            s = []
            while parent[j] != -1:
                s.append(j)
                j = parent[j]
            s.append(start)
            path[i] = s[::-1]
        return (dist[end], path[end]) if end >= 0 else (dist, path)


    def draw(self,surface):
        for node in self.nodes:
            succesors = self.get_succesors(node.value)
            for succesor in succesors:
                destiny = succesor[0]
                pg.draw.line(surface,(174,0,34),(node.x, node.y),(destiny.x, destiny.y),1)
                minx = node.x if node.x < destiny.x else destiny.x
                miny = node.y if node.y < destiny.y else destiny.y
                text = pg.font.SysFont(None, 20, True).render(str(succesor[1]),True,(81,0,255))
                surface.blit(text,((abs(destiny.x - node.x) / 2) + minx,(abs(destiny.y - node.y) / 2) + miny))
            node.draw(surface,5)