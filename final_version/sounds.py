from pygame import mixer


class Sounds:
    """Class to manage game sounds"""

    def __init__(self):
        """Initializes sounds"""

        mixer.init()
        self.bulletSound = mixer.Sound("sounds/laser.wav")
        self.collideSound = mixer.Sound("sounds/explosion.wav")
        self.hitSound = mixer.Sound("sounds/hit.wav")
        mixer.music.load("sounds/background.wav")
        mixer.music.play(-1)
