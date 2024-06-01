import random
import pygame
from src.bird import Bird
from src.pipe import Pipe


FLOOR_HEIGHT = 112
FLOOR_MOVEMENT_SPEED = 1


class Game:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.bird = Bird(screen, screen_width, screen_height, FLOOR_HEIGHT)
        self.score = None
        self.background = pygame.image.load(random.choice([r"assets/sprites/background-day.png",
                                                           r"assets/sprites/background-night.png"]))
        self.floor = pygame.image.load(r"assets/sprites/base.png")
        self.floor_position_left = 0
        self.floor_position_right = screen_width

    def display_title(self):
        return self.score

    def check_collision(self):
        pass

    def move_floor(self):
        self.floor_position_left -= FLOOR_MOVEMENT_SPEED
        self.floor_position_right -= FLOOR_MOVEMENT_SPEED
        if self.floor_position_left <= -self.screen_width:
            self.floor_position_left = self.screen_width
        if self.floor_position_right <= -self.screen_width:
            self.floor_position_right = self.screen_width

    def update(self):
        self.move_floor()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.floor, (self.floor_position_left, self.screen_height - FLOOR_HEIGHT))
        self.screen.blit(self.floor, (self.floor_position_right, self.screen_height - FLOOR_HEIGHT))
        self.bird.draw()
        pygame.display.flip()
