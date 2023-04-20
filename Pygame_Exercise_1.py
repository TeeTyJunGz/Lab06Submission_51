class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0,color = []):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.color = color

    def draw(self,screen):
        pg.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))
        
class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    def isMouseOn(self):
        px = pg.mouse.get_pos()[0]
        py = pg.mouse.get_pos()[1]
        if px >= self.x and px <= self.x + self.w and py >= self.y and py <= self.y + self.h:
            return True
        else:
            return False
    def isMousePress(self):
        px = pg.mouse.get_pos()[0]
        py = pg.mouse.get_pos()[1]
        if px >= self.x and px <= self.x + self.w and py >= self.y and py <= self.y + self.h:
            if pg.mouse.get_pressed()[0] == 1:
                return True
        else:
            return False
         
import sys 
import pygame as pg

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา

while(run):
    screen.fill((255, 255, 255))

    if btn.isMousePress():
        btn.color = 255,0,255
    elif btn.isMouseOn():
        btn.color = 130,130,130
    else:
        btn.color = 255,0,0
        
    btn.draw(screen)
    
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    