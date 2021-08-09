import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
import game_functions as gf
from button import Button


def run_game():
    """Init game."""
    # initialize pygame, settings and screen (surface)
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # make play button
    play_button = Button(ai_settings, screen, "Play")

    # create an instance to store game statistics
    stats = GameStats(ai_settings)

    # make a ship, a group of bullets, and a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # start the main loop of game
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)


run_game()
