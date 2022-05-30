import pygame

class Ship():
  def__init__(self, screen):
    """Initialize the ship image and set its starting position"""
  self.screen = screen

  #load the ship image and get its rect.
  self.image = pygame.image.load('images/ship.bmp')
  self.rect = self.image.get rect()
  self.screen_rect = self.screen_rect.bottom
  2