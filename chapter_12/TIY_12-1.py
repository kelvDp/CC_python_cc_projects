import sys
import pygame


class BlueSky:
    """Class to make blue pygame background"""

    def __init__(self):
        """Inits pygame with bg"""

        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("Blue Sky")
        self.bg_color = (0, 204, 204)

    def create_window(self):
        """Create pygame window"""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            pygame.display.flip()


if __name__ == "__main__":
    bs = BlueSky()
    bs.create_window()