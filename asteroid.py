import pygame
import random

from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            newa = random.uniform(20,50)
            n1asteroid = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
            n1asteroid.velocity = self.velocity.rotate(newa) * 1.2
            n2asteroid = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
            n2asteroid.velocity = self.velocity.rotate(-newa) * 1.2
