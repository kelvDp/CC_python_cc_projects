import sys
import pygame
from Alien_Invasion.chapter_12.game_char_class import GameCharacter


class Window:
    """Class to create window and character"""

    def __init__(self):
        """Inits pygame window and character"""

        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("Game Character")
        self.bg_color = (137, 137, 133)
        self.img = GameCharacter(self)

    def _handle_event(self):
        """Checks keyboard and mouse events"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Updates and flips screen"""

        self.screen.fill(self.bg_color)
        self.img.blit_img()
        pygame.display.flip()

    def open_window(self):
        """Opens pygame window"""

        while True:
            self._handle_event()
            self._update_screen()



if __name__ == "__main__":
    window = Window()
    window.open_window()

