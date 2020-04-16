from pygame import *
screen = display.set_mode((800,600))
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


    display.flip()
    myclock.tick(60)
quit()
