from math import sqrt
from pygame import *
from rocket import Rocket

class Game:
    def __init__(self):
        self.screen = None
        self.running = True
        self.width, self.height = 1080, 720

        self.rocket = None

    def on_init(self):
        init()
        display.set_caption("Orbital Mechanics")
        self.screen = display.set_mode((self.width, self.height))

        self.rocket = Rocket((self.width / 2, self.height / 4))

    def on_execute(self):
        self.on_init()
        while self.running:
            for _event in event.get():
                self.on_event(_event)
            self.on_loop()
            self.on_render()
        time.Clock().tick(60)
        self.on_cleanup()

    def on_event(self, events: event):
        if events.type == QUIT:
            self.running = False

    def on_loop(self):
        self.rocket.update()

    def on_render(self):
        self.screen.fill((255, 255, 255))

        # drawing earth
        draw.circle(self.screen, 255, (self.width / 2, self.height / 2), 20)

        # drawing rocket
        # draw.ellipse(self.screen, (255, 0, 0, 140), Rect(self.width / 2 - 270, self.height / 2 - 135 * sqrt(1 - 0.8 ** 2), 270, 270 * sqrt(1 - 0.8 ** 2)), width=5)
        self.screen.blit(self.rocket.sprite_image, self.rocket.rect)

        display.flip()

    def on_cleanup(self):
        quit()
