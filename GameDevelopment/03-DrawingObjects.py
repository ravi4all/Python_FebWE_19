import pygame
pygame.init()

screen = pygame.display.set_mode((1000,500))

white = 255,255,255
black = 0,0,0
screen.fill(white)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # surface, color, [x,y,w,h]
    pygame.draw.rect(screen,black,[0,0,50,50])
    # surface, color, [x,y], radius
    pygame.draw.circle(screen, black, [100,100], 50)

    pygame.display.update()