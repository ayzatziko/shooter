import time
import pygame
pygame.init()

class World(object):
    def __init__(self):
        self.run = True
        self.p = Player()
        self.bb = []
        self.e = Enemy()

    def process(self):
        for b in self.bb:
            b.process()
            if b.x > displayW or b.x < 0:
                self.bb.pop(self.bb.index(b))

        self.p.process()
        self.e.process()

        for b in self.bb:
            if b.x + b.r >= self.e.hitbox[0] and b.x - b.r <= self.e.hitbox[0] + self.e.hitbox[2] and b.y + b.r >= self.e.hitbox[1] and b.y - b.r <= self.e.hitbox[1] + self.e.hitbox[3]:
                self.bb.pop(self.bb.index(b))

        if self.e.hitbox[0] + self.e.hitbox[2] >= self.p.hitbox[0] and self.e.hitbox[0] <= self.p.hitbox[0] + self.p.hitbox[2] and self.e.hitbox[1] + self.e.hitbox[3] >= self.p.hitbox[1] and self.e.hitbox[1] <= self.p.hitbox[1] + self.p.hitbox[3]:
            self.p.health -= self.e.dmg
            self.p.x = 30
            self.p.y = 400

    def draw(self, win):
        self.p.draw(win)
        self.e.draw(win)
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
        self.hitbox = (self.x + 16, self.y + 16, self.w - 27, self.h - 20)
        self.health = 50

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
        if self.walkCount >= 27:
            self.walkCount = 0

        self.processJump()
        self.hitbox = (self.x + 16, self.y + 16, self.w - 27, self.h - 20)

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
        i = self.walkCount // 3
        if self.direct == self._standing: # standing
            win.blit(stand, (self.x, self.y))
        elif self.direct == self._right: # going right
            win.blit(walkRight[i], (self.x, self.y))
        elif self.direct == self._left: # going left
            win.blit(walkLeft[i], (self.x, self.y))
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

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

class Enemy(object):
    _left = -1
    _right = 1

    def __init__(self):
        self.x = 90
        self.y = 400
        self.w = 64
        self.h = 64
        self.v = 7
        self.lx = 40
        self.rx = displayW - 40
        self.direct = self._right
        self.walkCount = 0
        self.hitbox = (self.x + 15, self.y + 5, self.w - 30, self.h - 17)
        self.dmg = 15
        self.health = 100

    def process(self):
        self.walkCount += 1
        if self.walkCount >= 33:
            self.walkCount = 0

        if self.direct == self._right and self.x + self.w + (self.direct * self.v) >= self.rx:
            self.direct = self._left
        elif self.direct == self._left and self.x + (self.direct * self.v) <= self.lx:
            self.direct = self._right

        self.x += self.direct * self.v
        self.hitbox = (self.x + 15, self.y + 5, self.w - 40, self.h - 17)

    def draw(self, win):

        i = self.walkCount // 3
        if self.direct == self._right:
            win.blit(walkRightE[i], (self.x, self.y))
        else:
            win.blit(walkLeftE[i], (self.x, self.y))
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

caption = "Shooter"
displayW = 500
displayH = 500
fps = 27
world = World()

# images
walkRight = [pygame.image.load('R1.png'),pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png')]
walkRightE = [pygame.image.load('R1E.png'),pygame.image.load('R2E.png'),pygame.image.load('R3E.png'),pygame.image.load('R4E.png'),pygame.image.load('R5E.png'),pygame.image.load('R6E.png'),pygame.image.load('R7E.png'),pygame.image.load('R8E.png'),pygame.image.load('R9E.png'),pygame.image.load('R10E.png'),pygame.image.load('R11E.png')]
walkLeftE = [pygame.image.load('L1E.png'),pygame.image.load('L2E.png'),pygame.image.load('L3E.png'),pygame.image.load('L4E.png'),pygame.image.load('L5E.png'),pygame.image.load('L6E.png'),pygame.image.load('L7E.png'),pygame.image.load('L8E.png'),pygame.image.load('L9E.png'),pygame.image.load('L10E.png'),pygame.image.load('L11E.png')]
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
