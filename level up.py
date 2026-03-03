import pygame, random

pygame.init()

W, H = 600, 500
Speed = 5
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Times New Roman", 72)

bg = pygame.transform.scale(
    pygame.image.load("images (1).jpeg"), (W, H)
)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface((30, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect(
            topleft=(
                random.randint(0, W - 30),
                random.randint(0, H - 20)
            )
        )

    def move(self, dx, dy):
        self.rect.x = max(0, min(self.rect.x + dx, W - self.rect.width))
        self.rect.y = max(0, min(self.rect.y + dy, H - self.rect.height))

player = Sprite(pygame.Color("yellow"))
enemy = Sprite(pygame.Color("white"))
sprites = pygame.sprite.Group(player, enemy)

running = True
won = False

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or (
            e.type == pygame.KEYDOWN and e.key == pygame.K_x
        ):
            running = False

    if not won:
        keys = pygame.key.get_pressed()

        player.move(
            (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * Speed,
            (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * Speed
        )

        if player.rect.colliderect(enemy.rect):
            sprites.remove(enemy)
            won = True

    screen.blit(bg, (0, 0))
    sprites.draw(screen)

    if won:
        text = font.render("You Win", True, pygame.Color("white"))
        screen.blit(text, text.get_rect(center=(W // 2, H // 2)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()