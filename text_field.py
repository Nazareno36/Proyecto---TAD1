import pygame as pg

class TextField:

    def __init__(self,x,y,width,height):
        self.font = pg.font.Font(None,30)
        self.text = ''
        self.rect = pg.Rect((x,y,width,height))
        self.active = False
    
    def draw(self,surface):
        pg.draw.rect(surface,(215,214,227),self.rect)
        text_surface = self.font.render(self.text,True,(174,0,34))
        surface.blit(text_surface,(self.rect.x + 6,self.rect.y + 6))
        self.rect.w = max(self.rect.w,text_surface.get_width()+6)

