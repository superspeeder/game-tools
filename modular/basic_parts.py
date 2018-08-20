import pygame
from pygame.locals import SCRALPHA

class FilledRectangle(pygame.sprite.Sprite):
  def __init__(self, color, size, pos):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface(size)
    pygame.draw.rect(self.image, color, pygame.Rect((0,0), size)
