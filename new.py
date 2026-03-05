import pygame

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game 1")

clock = pygame.time.Clock()

x = 300
y = 200
speed = 5

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    pygame.draw.rect(screen, (0, 255, 0), (x, y, 50, 50))

    pygame.display.update()
    clock.tick(60)

pygame.quit()