import pygame as pg
from button import Button

class ComboBox:

    def __init__(self,x,y,w,h,options):
        self.active = False
        self.option = 0
        self.options = []
        self.rect = pg.Rect(x,y,w,h)
        for option in options:
            self.options.append(Button(x,y,w,h,option))
            y+=30

    def draw(self,surface, color):
        if not self.active:
            self.options[self.option].draw(surface,color)
        else:
            self.display(surface,color)
    
    def display(self,surface,color):
        self.options[self.option].draw(surface,color)
        for button in self.options:
            if button.text != self.options[self.option].text: 
                button.draw(surface,color)

    def set_option(self,option):
        temp = self.options[option].rect
        self.options[self.option].rect = temp
        self.options[option].rect = self.rect
        self.option = option
        self.active = False
    
    def update(self, event_pos):
        if self.active:
                    if self.rect.collidepoint(event_pos): self.active = False
                    i = 0
                    while i < len(self.options) and self.active:
                        if i != self.option and self.options[i].rect.collidepoint(event_pos):
                            self.set_option(i)
                        i+=1
        else:
            if self.rect.collidepoint(event_pos): self.active = True