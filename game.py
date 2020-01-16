import pygame
pygame.init()

caption = "Shooter"
displayW = 500
displayH = 500

win = pygame.display.set_mode((displayW, displayH))
pygame.display.set_caption(caption)

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
