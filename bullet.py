from math import radians

import cmath
import pygame

from config import BLACK

class Bullet:
    def __init__(self, position, speed, direction):
        self.position = position
        self.speed = speed
        self.direction = direction
        self.radius = 6

    def collides_with_player(self, player):
        a = self
        b = player
        d = self.position - player.pos
        distance = abs(d)
        # print(distance)
        if distance < a.radius + b.radius:
            return True
        else:
            return False

    def draw(self, sur):
        pygame.draw.circle(sur, BLACK, (int(self.position.real), int(self.position.imag)), self.radius)

    def update(self):
        step = cmath.rect(self.speed, radians(self.direction))
        self.position += step