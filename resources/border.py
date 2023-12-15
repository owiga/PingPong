import pygame

from settings import width, height, padding


class Border(pygame.rect.Rect):
    def __init__(self, game, top):
        self.game = game
        if top:
            self.pos = (padding, 2)
        else:
            self.pos = (padding, height - 22)
        self.scale = (width - padding * 2, 20)
        super().__init__(self.pos, self.scale)

    def draw(self):
        return pygame.draw.rect(self.game.screen, "red", self)
