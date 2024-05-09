from pygame import *
from math import *
from SpaceInvader_enemies import bezier_curve_calc  # For displaying curve trajectory purposes


class PlayerGlass(sprite.Sprite):
    def __init__(self):
        """Initializes the glass as a simple graphic sprite."""
        super().__init__()
        self.image = image.load("./assets/Water glass.png")
        self.image = transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()  # Creates hit box
        self.rect.x = 0
        self.rect.y = 400


class GoalGlass(sprite.Sprite):
    def __init__(self):
        """Initializes the goal glasses' sprite."""
        super().__init__()
        self.image = image.load("./assets/Water glass.png")
        self.image = transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 400


class Ball(sprite.Sprite):
    def __init__(self, player_glass_coord: tuple):
        """Initializes the Ball's sprite."""
        super().__init__()
        self.image = image.load("./assets/The BallTM.png")
        self.image = transform.scale(self.image, (25, 25))  # Rescales the sprite.
        self.rect = self.image.get_rect()  # Creates hit box
        # self.rect = Rect.inflate(self.rect, -15, -15) To see if we need rect redimensioning
        self.rect.center = player_glass_coord  # Centers it around the top of the player's glass.


class Vector(sprite.Sprite):
    def __init__(self, ball_topright: tuple):
        super().__init__()
        self.image = image.load("./assets/vecteur test.png")
        self.orig_image = self.image  # Keeps a copy of the original image to avoid loading it at each transformation.
        self.image = transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect(center=ball_topright)  # Puts the trajectory arrow near and above the ball for schematisation.
        self.pos = Vector2(ball_topright)  # Data for rotation management.
        self.offset = Vector2(10, -10)
        self.angle = 0  # Holds the essential data that will be used for the trajectory calculation.
        self.acceleration = 1

    def graphical_rotation(self, angle: int, length: int, ball):
        if 0 <= angle < 91 and 1 <= length <= 10:
            self.angle = angle
            self.acceleration = length  # Modifies the input data with the player's modifications.
            # Applies length and angle transformation to the arrow. To preserve its position, the offset vectors once
            # Rotated allows a recalibration of the position due to the rect modifications induced by image rotation.
            self.image = transform.rotozoom(self.orig_image, self.angle, 1)
            self.image = transform.scale(self.image, (25+length*5, 25+length*5))
            offset_rotation = self.offset.rotate(angle)
            self.rect = self.image.get_rect(center=self.pos+offset_rotation)  # Places the arrow at the desired
            # Corrected position.
            return True
        else:
            # If the player's modification induces entering wrong values, doesn't do anything.
            return False


class Game:
    def __init__(self):
        self.score = 0
        self.game_sprites = sprite.Group()
        self.player_glass = PlayerGlass()  # Instantiates the glass that will represent the player's.
        self.glass_goal = GoalGlass()  # Instantiates the glass surrounded by a few rects
        self.ball = Ball(self.player_glass.rect.midtop)
        self.vector = Vector(self.ball.rect.topright)
        self.game_sprites.add(self.player_glass)  # Adds successfully each sprite to the sprite group for display.
        self.game_sprites.add(self.glass_goal)
        self.game_sprites.add(self.ball)
        self.game_sprites.add(self.vector)
        self.launch = 0
        print(self.game_sprites.sprites())
