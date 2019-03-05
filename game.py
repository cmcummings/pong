"""

Pong game

"""
import sys, pygame
import utils.colors as color
from levels.pong import PongLevel
from config import SIZE


class Game:

    def __init__(self):
        # Initialize game
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE)

        # Intro level
        self.level = PongLevel()

        # Game loop
        while 1:
            self.tick()

    def tick(self):
        # Handle quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()

        self.level.tick(self.screen)

        pygame.display.flip() # Buffer


if __name__ == "__main__":
    Game()