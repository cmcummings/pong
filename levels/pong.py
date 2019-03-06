# pong.py
import pygame
from .level import Level
from objects.paddle import Paddle
from objects.ball import Ball
import utils.colors as color
from utils.res import load_font
from config import PLAYER1_CONTROLS, PLAYER2_CONTROLS, PADDLE_WIDTH, PADDLE_HEIGHT, WIDTH, HEIGHT
import random


class PongLevel(Level):
    """Level for the pong game."""

    def __init__(self):
        Level.__init__(self)

        self.score = [0, 0]
        self.score_font = load_font(None, 100)

        self.player1 = Paddle("Player1", 0, HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT, PLAYER1_CONTROLS)
        self.player2 = Paddle("Player2", WIDTH-PADDLE_WIDTH, HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT, PLAYER2_CONTROLS)
        self.ball = Ball("Ball", WIDTH/2, HEIGHT/2, 10, 10)
        
        self.add_object(self.player1, self.player2, self.ball)

    def tick(self, screen):
        self.logic()
        self.draw(screen)
        Level.tick(self, screen)

    def logic(self):
        if self.ball.ballrect.colliderect(self.player1.paddlerect):
            self.ball.bounce(x=True, speed_mult=1.1)
            self.player1.shrink(0.9)
        elif self.ball.ballrect.colliderect(self.player2.paddlerect):
            self.ball.bounce(x=True, speed_mult=1.1)
            self.player2.shrink(0.9)
            

        if self.ball.ballrect.left < 0:
            self.ball.respawn(1)
            self.player1.reset_size()
            self.player2.reset_size()
            self.score[1] += 1
        elif self.ball.ballrect.right > WIDTH:
            self.ball.respawn(-1)
            self.player1.reset_size()
            self.player2.reset_size()
            self.score[0] += 1

    def draw(self, screen):
        screen.fill(color.BLACK)

        # Draw the scores
        self.draw_score(screen, 0)
        self.draw_score(screen, 1)

        # Draw the dividing line
        divider = pygame.Rect(WIDTH/2-10, 0, 20, HEIGHT)
        pygame.draw.rect(screen, color.WHITE, divider)

    def draw_score(self, screen, player):
        score = self.score_font.render(str(self.score[player]), True, color.WHITE)
        score_rect = score.get_rect(y=50)
        if player == 0:
            score_rect.x = WIDTH/2 - score_rect.width * 2
        else:
            score_rect.x = WIDTH/2 + score_rect.width
        screen.blit(score, score_rect)


