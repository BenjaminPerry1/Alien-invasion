import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
#initialize game and create a screen object.
  #Initialize pygame, settings, and screen object.
  pygame.init()
  ai_settings = Settings()
  
  screen = pygame.display.set_mode((ai_settings.screen_width,                           ai_settings.screen_height))
  pygame.display.set_caption("Alien Invasion")
  #Make a ship.ship
  ship = Ship(screen)
  #Set the background color.
  bg_color = (230, 230, 230)
  #Start the main loop for the game.
  while True:
    #Watch for keyboard and mouse events.
    #Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          sys.exit()
    #Make the most recently drawn screen visible.
      pygame.display.flip()
      
run_game()

    