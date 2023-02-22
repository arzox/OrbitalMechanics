from pygame import *
import math


class Rocket(sprite.Sprite):
    def __init__(self, pos: tuple):
        super().__init__()
        self.sprite_image = image.load('assets/rocket.jpg').convert_alpha()
        self.sprite_image = transform.scale(self.sprite_image, (40, 40))
        self.sprite_image.set_colorkey([0, 0, 0])
        self.rect = self.sprite_image.get_rect()

        self.position = pos

        # orbital parameter
        self.start_posx = 540
        self.start_posy = 180
        self.semi_major_axis = 270
        self.gravitational_parameter = 4 * 10 ** 6
        self.eccentricity = 0.8
        self.average_pos = math.sqrt(self.gravitational_parameter / (self.semi_major_axis ** 3))
        # self.period = 2 * math.pi * math.sqrt((self.semi_major_axis ** 3) / self.gravitational_parameter)
        self.start_time = time.get_ticks()

    def getPos(self):
        mean_anomaly = self.average_pos * (time.get_ticks() / 1000 - self.start_time / 1000)
        true_anomaly = mean_anomaly + 2 * self.eccentricity * math.sin(mean_anomaly) + 1.25 * (
                    self.eccentricity ** 2) * math.sin(2 * mean_anomaly)
        dist = (self.semi_major_axis * (1 - self.eccentricity)) / (1 + self.eccentricity * math.cos(true_anomaly))
        print(true_anomaly)
        return math.cos(true_anomaly) * dist + 540, math.sin(true_anomaly) * dist + 360

    def update(self) -> None:
        self.rect.center = self.getPos()
