import pygame
from src.game import Game

SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


def main():
    game_instance = Game()
    running = True

    while running is True:
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
