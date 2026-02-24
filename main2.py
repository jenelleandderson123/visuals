import pygame

pygame.init()

window = pygame.display.set_mode((600,600))
window.fill((255, 255, 255))

Green = (0,255, 0)
pygame.draw.circle(window, Green, (300,300),50)

pygame.draw.circle(window, Green,(300,300),50, 3)

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
