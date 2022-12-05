import pygame as pg

class BinaryTree:

    class Node():

        def __init__(self,value) -> None:
            self.left = None
            self.right = None
            self.value = value
            self.x = 0
            self.y = 0
        
        def draw(self,surface,r):
            font = pg.font.Font(None,30)
            text_surface = font.render((str)(self.value),True,(174,0,34))
            pg.draw.circle(surface,(215,214,227),(self.x,self.y),r)
            surface.blit(text_surface,(self.x-(text_surface.get_width()/2),self.y-(text_surface.get_height()/2)))
    
    def __init__(self,value) -> None:
        self.root = self.Node(value)
    
    def insert(self, value):

        def balanced_insertion(root, value):
            if value < root.value:
                if root.left is None:
                    root.left = self.Node(value)
                else: balanced_insertion(root.left, value)
            elif value > root.value:
                if root.right is None:
                    root.right = self.Node(value)
                else: balanced_insertion(root.right, value)

        if self.root == None: self.root = self.Node(value) 
        else: balanced_insertion(self.root,value)
    
    def preorder_traversal(self):
        res = []
        def pro_t(node):
            if node:
                res.append(node.value)
                pro_t(node.left)
                pro_t(node.right)

        pro_t(self.root)
        return res

    def inorder_traversal(self):
        res = []
        def ino_t(node):
            if node:
                ino_t(node.left)
                res.append(node.value)
                ino_t(node.right)

        ino_t(self.root)
        return res
    
    def postorder_traversal(self):
        res = []
        def poo_t(node):
            if node:
                poo_t(node.left)
                poo_t(node.right)
                res.append(node.value)

        poo_t(self.root)
        return res
    
    def draw(self,surface):
        result = {}
        if self.root:
            i = 1
            self.root.x = 400
            self.root.y = 60
            r = 30
            delta = r*6.5
            result[i] = []
            result[i].append(self.root)
            self.root.draw(surface,r)
            while len(result[i]) > 0:
                result[i+1] = []
                for node in result[i]:
                    if node.left:
                        node.left.x = node.x-delta
                        node.left.y = node.y+60
                        pg.draw.line(surface,(174,0,34),(node.x,node.y),(node.left.x,node.left.y),2)
                        result[i+1].append(node.left)
                        node.left.draw(surface,r)
                    if node.right:
                        node.right.x = node.x+delta
                        node.right.y = node.y+60
                        pg.draw.line(surface,(174,0,34),(node.x,node.y),(node.right.x,node.right.y),2)
                        result[i+1].append(node.right)
                        node.right.draw(surface,r)
                i+=1
                r*=0.85
                delta*= 0.5