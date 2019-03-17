import pygame
pygame.init()

screen = pygame.display.set_mode((1000,500))

white = 255,255,255
screen.fill(white)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()