import pygame


class GameEngine:
    def __init__(self, width: int, height: int, title: str, fps: int = 60) -> None:
        pygame.init()
        self.window = pygame.display.set_mode((width, height))
        self.fps = fps
        pygame.display.set_caption(title)
        self.create()

    def run(self) -> None:
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.update()
            self._draw()
        pygame.quit()

    def create(self) -> None:
        ...

    def update(self) -> None:
        ...

    def draw(self) -> None:
        ...

    def _draw(self) -> None:
        self.draw()
        pygame.display.update()
