import pygame
from .bucket import Bucket
from .droplet import Droplet
from .game_engine import GameEngine

BACKGROUND_COLOR = (0, 0, 51)
WHITE_COLOR = (255, 255, 255)
DROP_COOLDOWN = 1250


class Drop(GameEngine):
    def create(self) -> None:
        self.bucket = Bucket()
        self.droplets: list[Droplet] = []
        self.drops_gathered = 0
        self.font = pygame.font.SysFont("comicsans", 28)
        self.spawn_rain_droplet()

    def update(self) -> None:
        self.bucket.update()
        if pygame.time.get_ticks() - self.last_drop_time >= DROP_COOLDOWN:
            self.spawn_rain_droplet()
        self.text = self.font.render(
            f"Drops collected: {self.drops_gathered}", 1, WHITE_COLOR
        )
        for droplet in self.droplets:
            droplet.update()
            if droplet.off_screen():
                self.droplets.remove(droplet)
            if self.bucket.overlap(droplet):
                self.drops_gathered += 1
                self.droplets.remove(droplet)

    def draw(self) -> None:
        self.window.fill(BACKGROUND_COLOR)
        self.bucket.draw(self.window)
        self.window.blit(self.text, (10, 10))
        for droplet in self.droplets:
            droplet.draw(self.window)

    def spawn_rain_droplet(self) -> None:
        self.droplets.append(Droplet())
        self.last_drop_time = pygame.time.get_ticks()
