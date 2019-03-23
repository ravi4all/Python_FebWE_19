import pygame, random
pygame.init()

height = 500
width = 1000
screen = pygame.display.set_mode((width, height))
white = 255,255,255
black = 0,0,0

img = pygame.image.load("frog.png")

imgWidth = img.get_width()
imgHeight = img.get_height()
imgX = random.randint(0, width - imgWidth)
imgY = random.randint(0, height - imgHeight)

x = 0
y = 0
moveX = 0
moveY = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveX = 1
                moveY = 0
            elif event.key == pygame.K_LEFT:
                moveX = -1
                moveY = 0
            elif event.key == pygame.K_DOWN:
                moveY = 1
                moveX = 0
            elif event.key == pygame.K_UP:
                moveY = -1
                moveX = 0

    screen.fill(white)
    screen.blit(img, (imgX, imgY))
    rect_1 = pygame.draw.rect(screen, black, [x,y,50,50])
    rect_2 = pygame.Rect(imgX, imgY, imgWidth, imgHeight)
    # pygame.draw.rect(screen, black, rect_2)
    x += moveX
    y += moveY

    if rect_1.colliderect(rect_2):
        imgX = random.randint(0, width - imgWidth)
        imgY = random.randint(0, height - imgHeight)

    if x > width:
        x = -50
    elif y > height:
        y = -50
    elif x < -50:
        x = width
    elif y < -50:
        y = height

    pygame.display.update()