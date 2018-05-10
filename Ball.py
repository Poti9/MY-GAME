import pygame


def sum_vectors(v, w):
    return(v[0]+w[0], v[1]+w[1])


class Ball():
    def __init__(self, color):
        self.radius = 15
        self.position = (400, 300)
        self.velocity = (0, -20)
        self.color = color

    def bounce(self):
        self.velocity = (self.velocity[0], -20)

    def update(self):
        self.position = sum_vectors(self.position, self.velocity)
        self.velocity = sum_vectors(self.velocity, (0, 1))

    def draw(self, s):
        pygame.draw.circle(s, self.color, self.position, self.radius)
