import pygame
pygame.init()

caption = "Shooter"
displayW = 500
displayH = 500
fps = 27
world = {
    'run': True,
    'vel': 5,
    'cx': 30, 'cy': 400, 'cw': 64, 'ch': 64,
    'isJump': False,
    'jumpHeight': 10,
    'jumpCount': 5,
    'walkCount': 0,
    'char_dir': 0,
}

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
            w['run'] = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        world['walkCount'] += 1
        world['char_dir'] = -1
        if w['cx'] <= w['vel']:
            pass
        else:
            w['cx'] = w['cx'] - w['vel']
    elif keys[pygame.K_RIGHT]:
        world['walkCount'] += 1
        world['char_dir'] = 1
        if w['cx'] + w['cw'] >= displayW - w['vel']:
            pass
        else:
            w['cx'] = w['cx'] + w['vel']

    if not w['isJump']:
        if keys[pygame.K_UP]:
            w['isJump'] = True
    else:
        h = w['jumpHeight']
        d = 1
        if h <= 0:
            d = -1

        w['jumpHeight'] -= 1
        if w['jumpHeight'] == -11:
            w['jumpHeight'] = 10
            w['isJump'] = False

        h = h ** 2 * d / 2
        w['cy'] = w['cy'] - h

    return w

def draw():
    win.blit(bg, (0, 0))

    if world['walkCount'] >= 27:
        world['walkCount'] = 0

    i = world['walkCount'] // 3
    if world['char_dir'] == 0: # standing
        win.blit(stand, (world['cx'], world['cy']))
    if world['char_dir'] == 1: # going right
        win.blit(walkRight[i], (world['cx'], world['cy']))
    if world['char_dir'] == -1: # going left
        win.blit(walkLeft[i], (world['cx'], world['cy']))

    pygame.display.update()

while world['run']:
    pygame.time.delay(fps)
    world = handle_events(world)
    draw()
    
pygame.quit()
