import cmath
from math import radians
import pygame

from bullet import Bullet
from config import WIDTH, HEIGHT, BLACK, GREY


class Player:
    def __init__(self, x, y, col):
        self.pos = x + y * 1j
        self.dir = 45
        self.radius = 25
        self.vel = 0
        self.vel_dir = 0
        self.color = col
        self.bullet = None
        self.health = 100

    def draw(self, sur):
        c = self.pos + cmath.rect(self.radius/2, radians(self.dir))
        d = self.pos + cmath.rect(1.5 * self.radius, radians(self.dir))
        pygame.draw.line(sur, BLACK, (int(c.real), int(c.imag)), (int(d.real), int(d.imag)), 10)
        pygame.draw.circle(sur, self.color, (int(self.pos.real), int(self.pos.imag)), self.radius)

        # its vector (-50, -(r+40))
        v = -50 - (self.radius+40)*1j
        healthbar_pos = self.pos + v
        # Draw backround of health
        pygame.draw.rect(sur, BLACK, (int(healthbar_pos.real), int(healthbar_pos.imag), 100, 20))
        # Draw health bar
        pygame.draw.rect(sur, GREY, (int(healthbar_pos.real) , int(healthbar_pos.imag), self.health, 20))


    def start_moving(self):
        self.vel = 7

    def stop_moving(self):
        self.vel = 0

    def start_rotating_left(self):
        self.vel_dir = -10

    def start_rotating_right(self):
        self.vel_dir = 10

    def stop_rotating(self):
        self.vel_dir = 0

    def start_moving_back(self):
        self.vel = -9

    def is_outside_screen(self):
        return self.pos.real >= WIDTH - self.radius or \
        self.pos.imag >= HEIGHT - self.radius or \
        self.pos.real < self.radius or \
        self.pos.imag < self.radius

    def collides_with_other_player(self, other_player):
        a = self
        b = other_player
        d = a.pos - b.pos
        distance = abs(d)
        # print(distance)
        if distance < a.radius + b.radius:
            return True
        else:
            return False

    def update(self, other_player):
        self.dir += self.vel_dir
        self.pos += cmath.rect(self.vel, radians(self.dir))
        if self.is_outside_screen():
            self.pos -= cmath.rect(self.vel, radians(self.dir))
        if self.collides_with_other_player(other_player):
            self.pos -= cmath.rect(self.vel, radians(self.dir))
        if self.bullet is not None:
            if self.bullet.collides_with_player(other_player):
                other_player.health -= 5
                self.bullet = None

    def fire_bullet(self):
        self.bullet = Bullet(self.pos, 15, self.dir)
        self.bullet = Bullet(self.pos, 15, self.dir)
