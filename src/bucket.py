import pygame
from .droplet import Droplet


class Bucket:
    def __init__(self) -> None:
        self.image = pygame.image.load("./images/bucket.png")
        self.rect = self.image.get_rect()
        self.window_size = pygame.display.get_surface().get_size()
        self.rect.x = self.window_size[0] // 2 - self.rect.width // 2
        self.rect.y = self.window_size[1] - self.rect.height - 20

    def update(self) -> None:
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.rect.x > 0:
            self.rect.x -= 5
        if (
            keys[pygame.K_d] or keys[pygame.K_RIGHT]
        ) and self.rect.x + self.rect.width < self.window_size[0]:
            self.rect.x += 5

    def draw(self, window: pygame.surface.Surface) -> None:
        window.blit(self.image, (self.rect))

    def overlap(self, droplet: Droplet) -> bool:
        return self.rect.colliderect(droplet.rect)
