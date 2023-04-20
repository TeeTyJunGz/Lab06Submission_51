class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height

    def draw(self,screen):
        pg.draw.rect(screen,(255,0,255),(self.x,self.y,self.w,self.h))
        
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
max_x, max_y = 50,50
val = 0.1
state = ''
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(max_x,max_y,100,100)

while(run):
        
    screen.fill((255, 255, 255))

    if state == 'W':
        max_y -= val
    elif state == 'S':
        max_y += val 
    elif state == 'A':
        max_x -= val
    elif state == 'D':
        max_x += val
    
    elif state == '0':
        pass
    
    btn = Button(max_x,max_y,100,100)
    btn.draw(screen)
    
    pg.display.update()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    
        if event.type == pg.KEYUP:
            state = '0'            
        elif event.type == pg.KEYDOWN and event.key == pg.K_w:
            state = 'W'
        elif event.type == pg.KEYDOWN and event.key == pg.K_a:
            state = 'A'
        elif event.type == pg.KEYDOWN and event.key == pg.K_s:
            state = 'S'
        elif event.type == pg.KEYDOWN and event.key == pg.K_d:
            state = 'D'