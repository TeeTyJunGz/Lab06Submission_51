class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0, text='', color = []):
        self.rect = pg.Rect(x, y, w, h)
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.text = text
        self.color = color
    def draw(self,screen):
        if self.text != '':
            itext = MFONT.render(self.text, True, (0,0,0))
            pg.draw.rect(screen,self.color,(self.x,self.y,itext.get_width()+20,itext.get_height()+20))
            screen.blit(itext, (self.x+10, self.y+10))
        else:
            pg.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0, text='', color = []):
        Rectangle.__init__(self, x, y, w, h, text, color)
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

class InputBox:

    def __init__(self, x, y, w, h, num , head='', text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.num = num
        self.head = head

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                txt = event.unicode
                if event.key == pg.K_RETURN:
                    # print(self.text)
                    # self.text = ''
                    pass
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if self.num:
                        if txt.isnumeric():
                            self.text += txt
                        else: 
                            pass
                    else:
                        self.text += txt
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        if self.head != '':
            htext = MFONT.render(self.head, True, (0,0,0))
            Screen.blit(htext, (self.rect.x, self.rect.y-20))
            
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(Screen, self.color, self.rect, 2)


                     
import sys
import pygame as pg

pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)
MFONT = pg.font.Font(None, 26)
input_box1 = InputBox(100, 100, 140, 32, False, 'Firstname') # สร้าง InputBox1
input_box2 = InputBox(100, 200, 140, 32, False, 'Lastname') # สร้าง InputBox2
input_box3 = InputBox(100, 300, 140, 32, True, 'Age') # สร้าง InputBox2

input_boxes = [input_box1, input_box2, input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย

state = ''
fftxt = ''

btn = Button(100, 350, 100, 50, 'Submit', (220,220,220))
run = True

while run:
    screen.fill((255, 255, 255))
    btn.draw(screen)
    btn.color = [220,220,220]

    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen

    if btn.isMousePress():
        btn.color = [127,127,127]
        if input_box1.text == '':
            state = 'Em'
            input_box1.color = [255,0,0]
        if input_box2.text == '':
            state = 'Em'
            input_box2.color = [255,0,0]
        if input_box3.text == '':
            state = 'Em'
            input_box3.color = [255,0,0]
        else:
            fftxt = 'Hello ' + str(input_box1.text) + ' ' + str(input_box2.text) + ' ! You are ' + str(input_box3.text) + ' years old.'
            state = 'Ok'
            
    if state == 'Em':
        htext = MFONT.render("Box is Empty", True, (0,0,0))
        screen.blit(htext, (100, 400))
    elif state == 'Ok':
        htext = MFONT.render(fftxt, True, (0,0,0))
        screen.blit(htext, (100, 400))
        
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(1)
    pg.display.update()