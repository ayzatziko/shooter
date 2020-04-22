# task: moving rectangle

import pygame

# vars
caption = "Caption"
display_config = (500, 500)


pygame.init()

win = pygame.display.set_mode(display_config)
pygame.display.set_caption(caption)
sleep_time = 27 # ms
background_color = (0, 0, 0) # (R, G, B), now black
run = True
rect_color = (0, 0, 255)
rect_shape = (120, 120, 40, 80)

# images
walk_right = [pygame.image.load('R1.png'),pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png')]
walk_left = [pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png')]
walk_right_e = [pygame.image.load('R1E.png'),pygame.image.load('R2E.png'),pygame.image.load('R3E.png'),pygame.image.load('R4E.png'),pygame.image.load('R5E.png'),pygame.image.load('R6E.png'),pygame.image.load('R7E.png'),pygame.image.load('R8E.png'),pygame.image.load('R9E.png'),pygame.image.load('R10E.png'),pygame.image.load('R11E.png')]
walk_left_e = [pygame.image.load('L1E.png'),pygame.image.load('L2E.png'),pygame.image.load('L3E.png'),pygame.image.load('L4E.png'),pygame.image.load('L5E.png'),pygame.image.load('L6E.png'),pygame.image.load('L7E.png'),pygame.image.load('L8E.png'),pygame.image.load('L9E.png'),pygame.image.load('L10E.png'),pygame.image.load('L11E.png')]
background_img = pygame.image.load('bg.jpg')
stand = pygame.image.load('standing.png')

# music
bullet_sound = pygame.mixer.Sound('bullet.wav')
hit_sound = pygame.mixer.Sound('hit.wav')
music = pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1) # infinite

# font
font = pygame.font.SysFont('comicsans', 30, True)

class Player:
	def __init__(self):
		self.x = 100
		self.y = 400
		self.v = 5

		# for jumping
		self.is_jump = False
		self.jump_count = 5
		self.jump_height = 10

	def process_jump(self):
		if not self.is_jump:
			return

		height = self.jump_height
		direction = 1
		if height <= 0:
			direction = -1

		self.jump_height -= 1
		if self.jump_height <= -11:
			self.jump_height = 10
			self.is_jump = False

		height = height ** 2 * direction / 2
		self.y = self.y - height

# players
p1 = Player()

while run:
	for event in pygame.event.get(): # catch events
		if event.type == pygame.QUIT: # actions on event types, only QUIT is handled now
			run = False

	hero_img = stand

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		new_x = p1.x - p1.v
		p1.x = new_x
		hero_img = walk_left[0]
		# make borders
	elif keys[pygame.K_RIGHT]:
		new_x = p1.x + p1.v
		p1.x = new_x
		hero_img = walk_right[0]
		# make borders
	if keys[pygame.K_UP]:
		p1.is_jump = True

	p1.process_jump()

	pygame.time.delay(sleep_time) # sleep
	win.blit(background_img, (0, 0))
	win.blit(hero_img, (p1.x, p1.y))
	pygame.display.update() # always update to show new display

pygame.quit()