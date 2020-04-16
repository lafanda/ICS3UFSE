#FSE ICS3U
from pygame import *
from math import *

screen = display.set_mode((800, 600))
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


myClock = time.Clock()
running = True
x = 100
y = 100

def tutorial():
    while running:
    mb = mouse.get_pressed()
    keys = key.get_pressed()
    for evt in event.get():
        if evt.type == QUIT:
            running = False

        if keys [K_w] == 1:
            y -= 10
        if keys [K_s] == 1:
             y += 10
        if keys [K_a] == 1:
            x -= 10
        if keys [K_d] == 1:
            x += 10


    mx, my = mouse.get_pos()  # move good guy



    screen.fill(BLACK)  # draw scene
    draw.circle(screen, GREEN, (x, y), 20)
    if mb[0] == 1:
        draw.rect(screen, RED, (x, y, -20, -40))
        print("hi")

page = "tutorial"
while page != "exit":
    if page == "tutorial"
        page = tutorial()



    display.flip()
    myClock.tick(60)  # delay (60 frames per second)

quit()

