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
        
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.ballrect)

    def bounce(self, x=False, y=False, speed_mult=1):
        if x: self.speed[0] = -self.speed[0]
        if y: self.speed[1] = -self.speed[1]
        self.speed[0] *= speed_mult
        self.speed[1] *= speed_mult

    def respawn(self, direction):
        self.ballrect.x, self.ballrect.y = self.start_pos
        self.speed = [direction, [-1, 1][random.randint(0, 1)]]

    def on_collide(self, collided_with):
        pass