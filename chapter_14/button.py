# Pygame doesn't have a built-in method for making buttons
# so we'll write a class to create a filled rect with a label:
import pygame.font  # lets Pygame render text to the screen.


class Button:
    """Class to create a button to take user-input"""

    def __init__(self, ai_game, msg):
        """Inits button attributes"""

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # set dimensions and props of button:
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # build button rect object and center it:
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # button msg needs to be prepped only once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into rendered img + center txt on btn"""

        self.msg_img = self.font.render(msg, True, self.text_color, self.button_color)
        # Boolean value to turn antialiasing on or off (antialiasing makes the
        # edges of the text smoother).

        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def draw_btn(self):
        """Draw blank btn and then msg"""

        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)
# We call screen.fill() to draw the rectangular portion of the button. Then
# we call screen.blit() to draw the text image to the screen, passing it an image
# and the rect object associated with the image.
