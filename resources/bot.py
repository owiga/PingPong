import pygame

from settings import player_color, height, width, block_y_padding


class Bot(pygame.rect.Rect):
    def __init__(self, game):
        self.game = game
        self.__width = 15
        self.__height = 80
        self.__pos = (width - 2 * (width // 32), height // 2)
        super().__init__(self.__pos, (self.__width, self.__height))

    def movement(self):
        ball_y = self.game.ball.rect[1]
        if ball_y > self.__pos[1] + self.height // 2:
            self.top = ball_y - 25
        elif ball_y < self.__pos[1] + self.height // 2:
            self.top = ball_y - 25
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_UP] and self.top > 17:
        #     self.move_ip(0, -2)
        # if keys[pygame.K_DOWN] and self.bottom < height - 24:
        #     self.move_ip(0, 2)

    def draw(self):
        return pygame.draw.rect(self.game.screen, player_color, self, border_radius=5)

    def _update(self):
        self.movement()
        self.draw()
