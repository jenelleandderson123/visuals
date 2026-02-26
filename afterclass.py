import pygame

pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Simple Game Screen")

white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)

font = pygame.font.SysFont(None, 36)
text = font.render("Hello Game!", True, black)

running = True
while running:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, blue, (150, 150, 200, 100))

    screen.blit(text, (170, 50))

    pygame.display.update()

pygame.quit()