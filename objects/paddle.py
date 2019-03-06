# paddle.py
import pygame
from utils.colors import WHITE
from .game_object import GameObject
from config import HEIGHT


class Paddle(GameObject):
    """Player for pong"""

    def __init__(self, obj_id, x, y, width, height, controls):
        GameObject.__init__(self, obj_id, x, y)
        self.controls = controls
        self.default_size = [width, height]

        self.paddlerect = pygame.Rect(x, y, width, height)

        self.speed = [0, 0]

    def logic(self):
        self.speed = [0, 0]

        pressed = pygame.key.get_pressed()
        if pressed[self.controls["up"]] == 1 and self.paddlerect.top > 0:
            self.speed[1] = -2
        if pressed[self.controls["down"]] == 1 and self.paddlerect.bottom < HEIGHT:
            self.speed[1] = 2

        self.paddlerect = self.paddlerect.move(self.speed)

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.paddlerect)

    def shrink(self, mult):
        self.paddlerect.height *= mult

    def reset_size(self):
        self.paddlerect.size = self.default_size