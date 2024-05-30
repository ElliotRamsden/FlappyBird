import random
import pygame
from src.bird import Bird
from src.pipe import Pipe


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load(random.choice([r"assets/sprites/background-day.png",
                                                           r"assets/sprites/background-night.png"]))

    def check_collision(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()
