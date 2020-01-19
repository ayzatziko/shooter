import time
import pygame
pygame.init()

class World(object):
    def __init__(self):
        self.run = True
        self.p = Player()
        self.bb = []

    def process(self):
        for b in self.bb:
            b.process()
            if b.x > displayW or b.x < 0:
                self.bb.pop(self.bb.index(b))

        self.p.process()

    def draw(self, win):
        self.p.draw(win)
        for b in self.bb:
            b.draw(win)

    def player_shoot(self):
        b = self.p.shoot()
        if b:
            self.bb.append(b)

class Player(object):
    _standing = 0
    _right = 1
    _left = -1
    _up = 1
    _down = -1

    def __init__(self):
        self.x = 30
        self.y = 400
        self.w = 64
        self.h = 64
        self.v = 5
        self.direct = 0
        self.isJump = False
        self.jumpCount = 5
        self.jumpHeight = 10
        self.walkCount = 0
        self.last_shot = 0

    def walkLeft(self):
        self.walkCount += 1
        self.direct = self._left
        if self.x > self.v:
            self.x -= self.v

    def walkRight(self):
        self.walkCount += 1
        self.direct = self._right
        if self.x + self.w < displayW - self.v:
            self.x += self.v

    def jump(self):
        if not self.isJump:
            self.isJump = True

    def processJump(self):
        if not self.isJump:
            return

        h = self.jumpHeight
        d = self._up
        if h <= 0:
            d = self._down

        self.jumpHeight -= 1
        if self.jumpHeight <= -11:
            self.jumpHeight = 10
            self.isJump = False

        h = h ** 2 * d / 2
        self.y = self.y - h

    def process(self):
        self.processJump()

    def shoot(self):
        n = int(time.time())
        if self.last_shot - n == 0:
            return False

        self.last_shot = n
        x = self.x + 25
        if self.direct == self._right:
            x = self.x + 30

        b = Bullet(x, self.y + 40, self.direct)
        return b

    def draw(self, win):
        if self.walkCount >= 27:
            self.walkCount = 0

        i = self.walkCount // 3
        if self.direct == self._standing: # standing
            win.blit(stand, (self.x, self.y))
        elif self.direct == self._right: # going right
            win.blit(walkRight[i], (self.x, self.y))
        elif self.direct == self._left: # going left
            win.blit(walkLeft[i], (self.x, self.y))

class Bullet(object):
    def __init__(self, x, y, direct):
        self.v = 8 * direct
        self.x = x
        self.y = y
        self.r = 6
        self.color = (0, 0, 0)

    def process(self):
        self.x += self.v

    def draw(self, win):
        pygame.draw.circle(win, self.color, (int(self.x), int(self.y)), self.r)

caption = "Shooter"
displayW = 500
displayH = 500
fps = 27
world = World()

# images
walkRight = [pygame.image.load('R1.png'),pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
stand = pygame.image.load('standing.png')

win = pygame.display.set_mode((displayW, displayH))
pygame.display.set_caption(caption)

def handle_events(w):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            w.run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        w.p.walkLeft()
    if keys[pygame.K_RIGHT]:
        w.p.walkRight()
    if keys[pygame.K_UP]:
        w.p.jump()
    if keys[pygame.K_SPACE]:
        w.player_shoot()

    w.process()

    return w

def draw():
    win.blit(bg, (0, 0))
    world.draw(win)
    pygame.display.update()

while world.run:
    pygame.time.delay(fps)
    world = handle_events(world)
    draw()
    
pygame.quit()
