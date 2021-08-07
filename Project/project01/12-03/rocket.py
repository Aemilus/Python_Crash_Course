import pygame


class Rocket:
    """Class for a rocket."""
    def __init__(self, screen):
        """Setup the rocket."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load("rocket.png")
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        # movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """Draw rocket image onto screen surface. This does not display the screen."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the position of rocket and prevent from moving out of screen edges."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.right += 1
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.left -= 1
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.top -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += 1
