from pygame import *
from random import *
screen = display.set_mode((800,600))
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
myclock = time.Clock()
running = True
x = 100
y = 100
enemyx = randint(50,700)
enemyy = randint(50,500)
face = "down"
def playerm(x,y,enemyx,enemyy,face):
    keys = key.get_pressed()
    if keys[K_w]==1:
        y-=5
        face = "up"
    if keys[K_s]==1:
        y+=5
        face = "down"
    if keys[K_a]==1:
        x-=5
        face = "left"
    if keys[K_d]==1:
        x+=5
        face = "right"
    screen.fill((0,0,0))
    draw.circle(screen,(255,255,255),(x,y),10)
    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()  # move good guy
    if mb[0] == 1:
        if face == "up":
            draw.rect(screen, RED, (x, y, -20, -40))
        if face == "right":
            draw.rect(screen, RED, (x, y, 40, -20))
        if face == "down":
            draw.rect(screen, RED, (x, y, 20, 40))
        if face == "left":
            draw.rect(screen, RED, (x, y, -40, 20))
    enemyRect=Rect(enemyx,enemyy,150,80)
    draw.rect(screen,BLUE,enemyRect)
def tutorial(running):
    while running:
        for evt in event.get():
            if evt.type==QUIT:
                running=False
        playerm(x,y,enemyx,enemyy,face)
        display.flip()
        myclock.tick(60)
tutorial(running)
quit()
