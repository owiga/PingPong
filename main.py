import random

import pygame
import sys

from settings import *
from resources.player import Player
from resources.border import Border
from resources.ball import Ball
from resources.bot import Bot


class Game:
    player: Player
    top_border: Border
    bot_border: Border
    ball: Ball
    bot: Bot

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((width, height))

    def load(self):
        self.player = Player(self)
        self.top_border = Border(self, True)
        self.bot_border = Border(self, False)
        self.ball = Ball(self)
        self.bot = Bot(self)

    def update(self):
        self.player._update()
        self.top_border.draw()
        self.bot_border.draw()
        self.ball._update()
        self.bot._update()

        pygame.display.flip()
        self.clock.tick(fps)

    def check_events(self):
        self.screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        self.load()
        while True:
            self.update()
            self.check_events()


if __name__ == '__main__':
    game = Game()
    game.run()
