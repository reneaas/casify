from .vector import Vector2d


def vektor(*args):
    if len([*args]) == 2:
        return Vektor2d(*args)
    else:
        return NotImplemented


def vinkel(a, b):
    if isinstance(a, Vektor2d) and isinstance(b, Vektor2d):
        return a.vinkel(b)
    else:
        raise TypeError("Vinkler kan bare regnes ut mellom to vektorer")


class Vektor2d(Vector2d):
    def __init__(self, x, y):
        super().__init__(x, y)

    @property
    def lengde(self):
        return self.length

    def vinkel(self, other):
        return self.angle(other)
