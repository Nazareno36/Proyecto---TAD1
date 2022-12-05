import pygame as pg

class Node:

        def __init__(self,value):
            self.x = 0
            self.y = 0
            self.parent = None
            self.value = value
            self.sons = []

        def draw(self,surface,r):
            font = pg.font.Font(None,30)
            text_surface = font.render((str)(self.value),True,(174,0,34))
            pg.draw.circle(surface,(215,214,227),(self.x,self.y),r)
            surface.blit(text_surface,(self.x-(text_surface.get_width()/2),self.y-(text_surface.get_height()/2)))

            



class Tree:

    def __init__(self,value):
        self.root = Node(value)

    def search(self,root,wanted):
        if root and root.value == wanted:
            return root
        else:
            for son in root.sons:
                finded = self.search(son,wanted)
                if finded and finded.value == wanted: return finded
            return None    

    def insert(self,parent,value):
        if not self.search(self.root,value):
            finded = self.search(self.root,parent)
            if finded:
                node = Node(value)
                node.parent = finded
                finded.sons.append(node)
                return True
        return False
        
    def to_dict(self):
        result = {}
        if self.root:
            i = 1
            result[i] = []
            result[i].append(self.root)
            while len(result[i]) > 0:
                result[i+1] = []
                for node in result[i]:
                    if len(node.sons)>0:
                        for son in node.sons:
                            result[i+1].append(son)
                i+=1
        result.popitem()
        return result
    
    def draw(self,surface):
        tree_dict = self.to_dict()
        y = 60

        lenght = -1
        for level in tree_dict.values():
            if len(level) > lenght:
                lenght = len(level)
        print(lenght)
        if lenght > 11: r = (790/lenght - 10)/2
        else: r = 30

        for level in tree_dict.values():
            x = ((800 - (10 + (2*r+10)*len(level)))/2)+10+r
            for node in level:
                node.x = x
                node.y = y
                if node.parent: 
                    pg.draw.line(surface,(174,0,34),(node.parent.x,node.parent.y),(x,y),2)
                    node.parent.draw(surface,r)
                node.draw(surface,r)
                x+=2*r+10
            y+=3*r+10



            

                        
