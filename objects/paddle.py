# paddle.py
import pygame
from utils.colors import WHITE
from .game_object import GameObject


class Paddle(GameObject):
    """Player for pong"""

    def __init__(self, obj_id, x, y, width, height, controls):
        GameObject.__init__(self, obj_id, x, y)
        self.controls = controls

        self.paddlerect = pygame.Rect(x, y, width, height)

        self.speed = [0, 0]

    def logic(self):
        pressed = pygame.key.get_pressed()
        if pressed[self.controls["up"]] is True:
            print("up")

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.paddlerect)
