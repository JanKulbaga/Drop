import pygame
import random


class Droplet:
    def __init__(self) -> None:
        self.image = pygame.image.load("./images/droplet.png")
        self.rect = self.image.get_rect()
        self.window_size = pygame.display.get_surface().get_size()
        self.rect.x = random.randint(0, self.window_size[0] - self.rect.width)
        self.rect.y = 0

    def update(self) -> None:
        self.rect.y += 5

    def draw(self, window: pygame.surface.Surface) -> None:
        window.blit(self.image, (self.rect))

    def off_screen(self) -> bool:
        return self.rect.y >= self.window_size[1]
