import pygame
pygame.init()

screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption("Sprite example")

image2 = pygame.image.load("download.jpeg")

x = 250
y = 150

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255,255,255))

    screen.blit(image2,(x,y))

    pygame.display.flip()

pygame.quit()