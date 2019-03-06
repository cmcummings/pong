# pong.py
from .level import Level
from objects.paddle import Paddle
from objects.ball import Ball
import utils.colors as colors
from config import PLAYER1_CONTROLS, PLAYER2_CONTROLS, PADDLE_WIDTH, PADDLE_HEIGHT, WIDTH, HEIGHT


class PongLevel(Level):
    """Level for the pong game."""

    def __init__(self):
        Level.__init__(self)

        self.player1 = Paddle("Player1", 0, HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT, PLAYER1_CONTROLS)
        self.player2 = Paddle("Player2", WIDTH-PADDLE_WIDTH, HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT, PLAYER2_CONTROLS)
        self.ball = Ball("Ball", WIDTH/2, HEIGHT/2, 10, 10)
        
        self.add_object(self.player1, self.player2, self.ball)

    def tick(self, screen):
        self.logic()
        self.draw(screen)
        Level.tick(self, screen)

    def logic(self):
        if self.ball.ballrect.colliderect(self.player1.paddlerect) or self.ball.ballrect.colliderect(self.player2.paddlerect):
            self.ball.speed[0] = -self.ball.speed[0]

    def draw(self, screen):
        screen.fill(colors.BLACK)

