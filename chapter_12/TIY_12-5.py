import sys
import pygame


class Keys:
    """Overall class to create and print keys"""

    def __init__(self):
        """Inits keys"""

        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("Keys")

    def get_keys(self):
        """Gets key events and prints it"""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(event.key)
                    if event.key == pygame.K_q:
                        sys.exit()
                    else:
                       print(event.key)


if __name__ == "__main__":
    key = Keys()
    key.get_keys()