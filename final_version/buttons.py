import pygame.font


class EasyBtn:
    """Class to create a button to take user-input"""

    def __init__(self, game, msg):
        """Inits button attributes"""

        self.screen = game.screen
        self.width, self.height = 150, 50
        self.btn_color = (51, 255, 51)
        self.txt_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(450, 359, self.width, self.height)
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turns msg into rendered img and centers text on btn"""

        self.msg_img = self.font.render(msg, True, self.txt_color, self.btn_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def draw_btn(self):
        """Draws button and message on screen"""

        self.screen.fill(self.btn_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)


class MediumBtn:
    """Class to create a button to take user-input"""

    def __init__(self, game, msg):
        """Inits button attributes"""

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 150, 50
        self.btn_color = (255, 255, 0)
        self.txt_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turns msg into rendered img and centers text on btn"""

        self.msg_img = self.font.render(msg, True, self.txt_color, self.btn_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def draw_btn(self):
        """Draws button and message on screen"""

        self.screen.fill(self.btn_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)


class HardBtn:
    """Class to create a button to take user-input"""

    def __init__(self, game, msg):
        """Inits button attributes"""

        self.screen = game.screen
        self.width, self.height = 150, 50
        self.btn_color = (255, 0, 0)
        self.txt_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(766, 359, self.width, self.height)

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turns msg into rendered img and centers text on btn"""

        self.msg_img = self.font.render(msg, True, self.txt_color, self.btn_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def draw_btn(self):
        """Draws button and message on screen"""

        self.screen.fill(self.btn_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)
