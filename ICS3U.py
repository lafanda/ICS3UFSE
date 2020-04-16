from pygame import *
from random import *

screen = display.set_mode((800, 600))
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
myclock = time.Clock()
running = True
enemyx = randint(50, 700)
enemyy = randint(50, 500)
enemyCol = GREEN
face = "down"
x = 200
y = 200
def playerm():
    global x, y, face, swordRect, mb
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

    
    draw.circle(screen,(255,255,255),(x,y),10)
    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()  # move good guy
    if face == "up":
        swordRect = Rect(x, y-40, 20, 40)
    if face == "right":
        swordRect = Rect(x, y, 40, 20)
    if face == "down":
        swordRect = Rect(x-20, y, 20, 40)
    if face == "left":
        swordRect = Rect(x-40, y-20, 40, 20)
    if mb[0] == 1:
        draw.rect(screen,BLUE,swordRect)
    

    

def tutorial(running):
    while running:
        for evt in event.get():
            if evt.type==QUIT:
                running=False
        screen.fill((0,0,0))

        playerm()
        enemyRect = Rect(enemyx, enemyy, 25, 25)
        draw.rect(screen, GREEN, enemyRect)
        if mb[0] == 1:
            if swordRect.colliderect(enemyRect):
                draw.rect(screen, RED, enemyRect)

        display.flip()
        myclock.tick(60)
        print(myClock.get_ticks)
tutorial(running)
quit()
