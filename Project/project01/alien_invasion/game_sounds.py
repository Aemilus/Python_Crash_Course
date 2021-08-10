import pygame.mixer
from time import sleep


class LevelUpSound:
    """A class for handling level up sound during game."""
    def __init__(self):
        pygame.mixer.init()
        self.sound_filepath = "sounds/level_up.wav"
        self.sound = pygame.mixer.Sound(self.sound_filepath)

    def play_sound(self):
        self.sound.play()
        sleep(1)
