import pygame
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1

class CustomSprite(pygame.sprite.Sprite):
    def __init__(self, color, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def change_color(self):
        self.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Color Change")
all_sprites = pygame.sprite.Group(CustomSprite((255, 0, 0), 100), CustomSprite((0, 0, 255), 100))

all_sprites.sprites()[0].rect.topleft = (100, 100)
all_sprites.sprites()[1].rect.topleft = (300, 100)

running = True
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)  # Trigger event every 2 seconds
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_COLOR_EVENT:
            for sprite in all_sprites:
                sprite.change_color()

    screen.fill((255, 255, 255))  # Clear screen
    all_sprites.draw(screen)        # Draw sprites
    pygame.display.flip()           # Update display
    pygame.time.Clock().tick(FPS)   # Cap frame rate

pygame.quit()