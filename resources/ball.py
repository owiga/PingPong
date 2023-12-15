import pygame
import random

from settings import height, width, ball_color

psevdo = [0, 1, 1, 0, 0, 1]


class Ball(pygame.rect.Rect):
    def __init__(self, game):
        self.game = game
        self.radius = 8
        self.vx = random.randint(-2, 2)
        while self.vx == 0:
            self.vx = random.randint(-2, 2)
        self.vy = random.randint(-2, 2)
        while self.vy == 0:
            self.vy = random.randint(-2, 2)
        self.rect = pygame.Rect(width // 2 - self.radius, height // 2 - self.radius, 2 * self.radius, 2 * self.radius)
        super().__init__(self.rect)

    def movement(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if self.rect.colliderect(self.game.top_border.draw()) or self.rect.colliderect(self.game.bot_border.draw()):
            self.vy = -self.vy
        if self.rect.colliderect(self.game.player.draw()):
            self.vx = -self.vx
            if random.choice(psevdo) == 1:
                self.vx = random.randint(2, 4)
                while self.vx == 0:
                    self.vx = random.randint(-2, 2)
        elif self.rect.colliderect(self.game.bot.draw()):
            self.vx = -self.vx
            if random.choice(psevdo) == 1:
                self.vx = random.randint(-4, -2)
                while self.vx == 0:
                    self.vx = random.randint(-2, 2)

    def draw(self):
        pygame.draw.circle(self.game.screen, ball_color, (self.rect[0] + self.radius, self.rect[1] + self.radius),
                           self.radius)

    def _update(self):
        self.movement()
        self.draw()
