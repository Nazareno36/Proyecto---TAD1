import pygame as pg

class Button:

    def __init__(self,x,y,width,height,text):
        self.rect = pg.Rect((x,y,width,height))  
        self.actioned = False
        self.font = pg.font.Font(None,30)
        self.text = text
    
    def draw(self,surface, color):
        pg.draw.rect(surface,color,self.rect)
        text_surface = self.font.render(self.text,True,(0,0,0))
        surface.blit(text_surface,(self.rect.x +5,self.rect.y+5))
    
    def translate(self,x,y):
        self.rect.x = x
        self.rect.y = y
