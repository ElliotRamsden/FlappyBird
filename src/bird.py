import pygame

BIRD_WIDTH = 34
BIRD_HEIGHT = 24


class Bird:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.bird_image = pygame.image.load(r"assets/sprites/bluebird-upflap.png")
        self.rectangle = self.bird_image.get_rect()
        self.rectangle.center = (screen_width // 4, screen_height // 2)
        self.velocity = 0

    def update(self):
        pass

    def jump(self):
        pass

    def draw(self):
        self.screen.blit(self.bird_image, self.rectangle)
