import pygame

pygame.init()

screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Sprite example")

image_unk = pygame.image.load("images.png")

x = 250
y = 150
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
            
    screen.fill((255, 255, 255))
    
    screen.blit(image_unk, (x, y))
    
    pygame.display.flip()

pygame.quit()
