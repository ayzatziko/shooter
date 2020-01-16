import pygame
pygame.init()

caption = "Shooter"
displayW = 500
displayH = 500
fps = 100
run = True
bg = (0, 0, 0)
world = {'rect': (50, 50, 40, 60), 'color': (255, 0, 0), 'vel': 5}

win = pygame.display.set_mode((displayW, displayH))
pygame.display.set_caption(caption)

def handle_events(w):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        w['rect'] = (w['rect'][0] - w['vel'], w['rect'][1], w['rect'][2], w['rect'][3])
    elif keys[pygame.K_RIGHT]:
        w['rect'] = (w['rect'][0] + w['vel'], w['rect'][1], w['rect'][2], w['rect'][3])
    elif keys[pygame.K_UP]:
        pass

    return w

def draw():
    win.fill(bg)
    pygame.draw.rect(win, world['color'], world['rect'])
    pygame.display.update()

while run:
    pygame.time.delay(fps)
    world = handle_events(world)
    draw()
    
pygame.quit()
