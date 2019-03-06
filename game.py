"""

Pong game

"""
import sys, pygame
import utils.colors as color
from levels.pong import PongLevel
from levels.main_menu import MainMenuLevel
from config import SIZE

ONE_PLAYER = "1P"
TWO_PLAYER = "2P"
MAIN_MENU = "MAIN MENU"

class Game:

    def __init__(self):
        # Initialize game
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption("Pong")

        # Intro level
        self.level = MainMenuLevel()

        # Game loop
        while 1:
            self.tick()

    def tick(self):
        # Handle quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()

        self.level.tick(self)

        pygame.display.flip() # Buffer

    def change_level(self, level):
        if level == ONE_PLAYER:
            self.level = PongLevel(1)
        elif level == TWO_PLAYER:
            self.level = PongLevel(2)
        elif level == MAIN_MENU:
            self.level = MainMenuLevel()


if __name__ == "__main__":
    Game()