import pygame
from src.game import Game

SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
favicon = pygame.image.load(r"assets/favicon.ico")
pygame.display.set_icon(favicon)
clock = pygame.time.Clock()


def main():
    game_instance = Game(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
    running = True

    while running is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_instance.update()
        game_instance.draw()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
