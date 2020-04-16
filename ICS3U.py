from pygame import *
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
while running:
    keys = key.get_pressed()

    for evt in event.get():
        if evt.type == QUIT:
            running == False
    if keys[K_w]==1:
        y-=5
    if keys[K_s]==1:
        y+=5
    if keys[K_a]==1:
        x-=5
    if keys[K_d]==1:
        x+=5
    screen.fill((0,0,0))
    draw.circle(screen,(255,255,255),(x,y),10)
    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()  # move good guy
    if mb[0] == 1:
        draw.rect(screen, RED, (x, y, -20, -40))
        print("hi")
    display.flip()
    myclock.tick(60)
quit()
