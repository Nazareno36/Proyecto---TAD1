import pygame as pg

class Card:
    
    def __init__(self,value,path):
        self.value = value
        self.rect = pg.Rect((0,0,120,160))
        self.image = pg.transform.scale(pg.image.load(path),(120,160))
    
    def draw(self,surface):
        surface.blit(self.image,(self.rect.x,self.rect.y))
    
    def translate(self,x,y):
        self.rect.x = x
        self.rect.y = y

    def transform(self,width,height):
        self.rect.w = width
        self.rect.h = height
        self.image = pg.transform.scale(self.image,(width,height))
    