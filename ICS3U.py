from pygame import *
from random import *

screen = display.set_mode((800, 600))
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
myclock = time.Clock()

class Player:
    def __init__(self,x,y,face):
        playerPic=image.load('C:/Users/Abid/Documents/GitHub/ICS3UFSE/images/Sprite.png')
        self.x = x
        self.y = y
        self.face = face
        self.sprite = playerPic
    def render(self):
        screen.blit(self.sprite,(self.x-13,self.y-13))
    def movement(self):
        keys = key.get_pressed()
        if keys[K_w]==1:
            self.y-= 3
            self.face = "up"
        if keys[K_s]==1:
            self.y+= 3
            self.face = "down"
        if keys[K_a]==1:
            self.x-= 3
            self.face = "left"
        if keys[K_d]==1:
            self.x+= 3
            self.face = "right"

    def sword(self):
        mb = mouse.get_pressed()
        mx, my = mouse.get_pos()  # move good guy
        if self.face == "up":
            swordRect = Rect(self.x, self.y-40, 20, 40)
        if self.face == "right":
            swordRect = Rect(self.x, self.y, 40, 20)
        if self.face == "down":
            swordRect = Rect(self.x-20, self.y, 20, 40)
        if self.face == "left":
            swordRect = Rect(self.x-40, self.y-20, 40, 20)
        if mb[0] == 1:
            draw.rect(screen, BLUE, swordRect)
        self.hitbox = swordRect
class Enemy:
    def __init__(self, enemyx, enemyy):
        enemyPic=image.load('C:/Users/Abid/Documents/GitHub/ICS3UFSE/images/Sprite2.png')
        delete = True
        self.enemyx = enemyx
        self.enemyy = enemyy
        self.sprite = enemyPic
        self.delete = delete
        enemyRect = Rect(enemyx, enemyy, 25, 25)
        draw.rect(screen, GREEN, enemyRect)
        self.hurtbox = enemyRect
    def render(self):
        screen.blit(self.sprite,(self.enemyx,self.enemyy))
    def collision(self):
        if player.hitbox.colliderect(self.hurtbox):
            return self.delete == True

class Level:
    def __init__(self):
        levels = ["Tutorial", "Level1"]
        level = "Tutorial"


Enemyx = randint(50, 500)
Enemyy = randint(50, 500)
player = Player(200,200,"down")
enemy = Enemy(Enemyx, Enemyy)
running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
    screen.fill((0, 0, 0))
    classes = [player.render(), player.movement(),player.sword(),enemy.render(),enemy.collision()]
    if enemy.collision() == True:
        classes.remove(enemy.collision())
        classes.remove(enemy.render())
    for i in classes:
        i
    print(classes)
    display.flip()
    myclock.tick(60)
    


quit()
