import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
from button import Button
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard

def run_game():
    # Initialize pygame, settings and the screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")

    # Create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    alien_bullets = Group()
    bullets = Group()
    aliens = Group()
    
    # create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # make the play button
    play_button = Button(ai_settings, screen, "Play")
 
    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            bullets.update()
            alien_bullets.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets) 
            gf.update_alien_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets)     
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, play_button)

run_game()

 