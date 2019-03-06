# ball.py
import pygame, random
from .game_object import GameObject
from utils.res import load_resource
from config import WIDTH, HEIGHT
from utils.colors import WHITE


class Ball(GameObject):

    def __init__(self, obj_id, x, y, width, height):
        GameObject.__init__(self, obj_id, x, y)
        self.start_pos = x, y
        self.speed = [1, 1]
        
        self.ballrect = pygame.Rect(x, y, width, height)

    def logic(self):
        self.ballrect = self.ballrect.move(self.speed)
        if self.ballrect.top < 0 or self.ballrect.bottom > HEIGHT:
            self.speed[1] = -self.speed[1]


        if self.ballrect.left < 0:
            self.ballrect.x, self.ballrect.y = self.start_pos
            self.speed = [1, [-1, 1][random.randint(0, 1)]]
        elif self.ballrect.right > WIDTH:
            self.ballrect.x, self.ballrect.y = self.start_pos
            self.speed = [-1, [-1, 1][random.randint(0, 1)]]
        
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.ballrect)