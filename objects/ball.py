# ball.py
import pygame
from .game_object import GameObject
from utils.res import load_resource
from config import WIDTH, HEIGHT
from utils.colors import WHITE


class Ball(GameObject):

    def __init__(self, obj_id, x, y, width, height):
        GameObject.__init__(self, obj_id, x, y)

        self.ballrect = pygame.Rect(x, y, width, height)

        self.speed = [1, 1]

    def logic(self):
        self.ballrect = self.ballrect.move(self.speed)
        if self.ballrect.left < 0 or self.ballrect.right > WIDTH:
            self.speed[0] = -self.speed[0]
        if self.ballrect.top < 0 or self.ballrect.bottom > HEIGHT:
            self.speed[1] = -self.speed[1]

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.ballrect)