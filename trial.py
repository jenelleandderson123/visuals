import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

sprite_size = 50
x = WIDTH // 2
y = HEIGHT // 2
speed = 5
color = (0, 128, 255)

running = True
while running:
    clock.tick(60)
    
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

    hit_boundary = False

    if x <= 0:
        x = 0
        hit_boundary = True
    if x + sprite_size >= WIDTH:
        x = WIDTH - sprite_size
        hit_boundary = True
    if y <= 0:
        y = 0
        hit_boundary = True
    if y + sprite_size >= HEIGHT:
        y = HEIGHT - sprite_size
        hit_boundary = True

    if hit_boundary:
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, color, (x, y, sprite_size, sprite_size))
    pygame.display.flip()

pygame.quit()
sys.exit()