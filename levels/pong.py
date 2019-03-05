# pong.py
from .level import Level
from objects.paddle import Paddle
from objects.ball import Ball
import utils.colors as colors
from config import PLAYER1_CONTROLS, PLAYER2_CONTROLS


class PongLevel(Level):
    """Level for the pong game."""

    def __init__(self):
        Level.__init__(self)

        player1 = Paddle("Player1", 0, 0, 20, 100, PLAYER1_CONTROLS)
        player2 = Paddle("Player2", 0, 0, 20, 100, PLAYER2_CONTROLS)
        ball = Ball("Ball", 640, 360, 10, 10)
        
        self.add_object(player1, player2, ball)

    def tick(self, screen):
        screen.fill(colors.BLACK)
        
        Level.tick(self, screen)
