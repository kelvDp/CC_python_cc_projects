import sys
import pygame


class AlienInvasion:
    """Overall class to manage game behavior and assets"""

    def __init__(self):
        """Init the game and create game resources"""

        pygame.init()  # nitializes the background settings that Pygame needs to work properly
        self.screen = pygame.display.set_mode((1200, 800))  # sets display size
        pygame.display.set_caption("Alien Invasion")  # sets caption on display

    def run_game(self):
        """Starts main loop for game"""

        while True:
            # watch for keyboard+mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # make most recently drawn screen visible
            pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance and run game
    ai = AlienInvasion()
    ai.run_game()
# We place run_game() in an if block that only runs if the file is called
# directly
