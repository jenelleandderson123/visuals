import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (50, 50, 50)
SPRITE1_COLOR = (255, 0, 0)
SPRITE2_COLOR = (0, 255, 0)
SPRITE_SIZE = 50
MOVEMENT_SPEED = 5

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Sprite Control")
clock = pygame.time.Clock()

sprite1_x = 100
sprite1_y = SCREEN_HEIGHT // 2 - SPRITE_SIZE // 2
sprite2_x = SCREEN_WIDTH - 150
sprite2_y = SCREEN_HEIGHT // 2 - SPRITE_SIZE // 2

moving_up = False
moving_down = False
moving_left = False
moving_right = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moving_up = True
            elif event.key == pygame.K_DOWN:
                moving_down = True
            elif event.key == pygame.K_LEFT:
                moving_left = True
            elif event.key == pygame.K_RIGHT:
                moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                moving_up = False
            elif event.key == pygame.K_DOWN:
                moving_down = False
            elif event.key == pygame.K_LEFT:
                moving_left = False
            elif event.key == pygame.K_RIGHT:
                moving_right = False
    
    if moving_up:
        sprite1_y -= MOVEMENT_SPEED
    if moving_down:
        sprite1_y += MOVEMENT_SPEED
    if moving_left:
        sprite1_x -= MOVEMENT_SPEED
    if moving_right:
        sprite1_x += MOVEMENT_SPEED
    
    if sprite1_x < 0:
        sprite1_x = 0
    if sprite1_x > SCREEN_WIDTH - SPRITE_SIZE:
        sprite1_x = SCREEN_WIDTH - SPRITE_SIZE
    if sprite1_y < 0:
        sprite1_y = 0
    if sprite1_y > SCREEN_HEIGHT - SPRITE_SIZE:
        sprite1_y = SCREEN_HEIGHT - SPRITE_SIZE
    
    screen.fill(BACKGROUND_COLOR)
    
    pygame.draw.rect(screen, SPRITE1_COLOR, (sprite1_x, sprite1_y, SPRITE_SIZE, SPRITE_SIZE))
    pygame.draw.rect(screen, SPRITE2_COLOR, (sprite2_x, sprite2_y, SPRITE_SIZE, SPRITE_SIZE))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()