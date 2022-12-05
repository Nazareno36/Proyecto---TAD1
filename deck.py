import pygame as pg
from stack import Stack
from card import Card

class Deck:

    def __init__(self,x,y):
        self.stack = Stack()
        self.rect = pg.Rect((x,y,120,160))

    def draw(self,surface):
        current_node = self.stack.head
        while current_node:  
            current_node.value.draw(surface)
            current_node = current_node.next

    def push(self,card: Card):
        if self.stack.tail:
            card.translate(self.stack.tail.value.rect.x + 10,self.stack.tail.value.rect.y + 20)
            self.stack.push_back(card)
        else:
            card.translate(self.rect.x,self.rect.y)
            self.stack.push_back(card)
        self.rect.y+=20
        self.rect.x+=10
    
    
    def pop(self):
        if self.stack.len > 0:
            card = self.stack.pop_node()
            if card: 
                self.rect.y-=20 
                self.rect.x-=10 
            return card
    
    def is_ordered(self) -> bool:
        ordered = self.stack.len == 13
        i = 14
        current_node = self.stack.head
        while current_node and ordered:  
            if current_node.value.value != i: ordered = False
            current_node = current_node.next
            i-=1
        return ordered