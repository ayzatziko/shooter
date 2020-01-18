import pygame
pygame.init()

caption = "Shooter"
displayW = 500
displayH = 500
fps = 27
bg = (0, 0, 0)
world = {'run': True, 'rect': (50, 400, 40, 60), 'color': (255, 0, 0), 'vel': 5, 'isJump': False, 'jumpHeight': 10, 'jumpCount': 5}

win = pygame.display.set_mode((displayW, displayH))
pygame.display.set_caption(caption)

def handle_events(w):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            w['run'] = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if w['rect'][0] <= w['vel']:
            pass
        else:
            w['rect'] = (w['rect'][0] - w['vel'], w['rect'][1], w['rect'][2], w['rect'][3])
    elif keys[pygame.K_RIGHT]:
        if w['rect'][0] + w['rect'][2] >= displayW - w['vel']:
            pass
        else:
            w['rect'] = (w['rect'][0] + w['vel'], w['rect'][1], w['rect'][2], w['rect'][3])

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
        w['rect'] = (w['rect'][0], w['rect'][1] - h, w['rect'][2], w['rect'][3])

    return w

def draw():
    win.fill(bg)
    pygame.draw.rect(win, world['color'], world['rect'])
    pygame.display.update()

while world['run']:
    pygame.time.delay(fps)
    world = handle_events(world)
    draw()
    
pygame.quit()
