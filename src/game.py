import random
import pygame
from src.bird import Bird
from src.pipe import Pipe


class Game:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.bird = Bird(screen, screen_width, screen_height)
        self.score = 0
        self.background = pygame.image.load(random.choice([r"assets/sprites/background-day.png",
                                                           r"assets/sprites/background-night.png"]))
        self.floor = pygame.image.load(r"assets/sprites/base.png")

    def check_collision(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.bird.draw()
        pygame.display.flip()
