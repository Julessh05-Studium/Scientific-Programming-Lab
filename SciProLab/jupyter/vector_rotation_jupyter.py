from models.complex import ComplexNumber
from math import cos, pi, sin


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def rotate(self, angle):
        c = ComplexNumber(self.x, self.y)
        rad = angle * (pi / 180)
        # real * cos = real number.
        # imag * sin = real number, because imag and sin each contain i (i^2 = -1).
        # real * sin = imag number, because sin contains i.
        # imag * cos = imag number, because imag contains i.
        rotated_real = c.real * cos(rad) - c.imag * sin(rad)
        rotated_imag = c.real * sin(rad) + c.imag * cos(rad)
        rotated_c = ComplexNumber(rotated_real, rotated_imag)
        return Vector(rotated_c.real, rotated_c.imag)
