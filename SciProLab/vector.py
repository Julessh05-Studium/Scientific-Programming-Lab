from complex import ComplexNumber
from math import cos, pi, sin

from errors.VectorEqualError import VectorEqualError
from errors.VectorTypeError import VectorTypeError


class Vector:

    def __init__(self, x, y):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self.x = x
            self.y = y
        else:
            raise VectorTypeError()

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise VectorTypeError

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        raise VectorTypeError

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        raise VectorEqualError

    def rotate_complete(self, angle):
        if not isinstance(angle, (int, float)):
            raise VectorTypeError()
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

    def rotate(self, angle):
        if not isinstance(angle, (int, float)):
            raise VectorTypeError()
        c = ComplexNumber(self.x, self.y)
        rad = angle * (pi / 180)
        # real * cos = real number.
        # imag * sin = real number, because imag and sin each contain i (i^2 = -1).
        # real * sin = imag number, because sin contains i.
        # imag * cos = imag number, because imag contains i.
        rotated_real = round(c.real * cos(rad) - c.imag * sin(rad))
        rotated_imag = round(c.real * sin(rad) + c.imag * cos(rad))
        rotated_c = ComplexNumber(rotated_real, rotated_imag)
        return Vector(rotated_c.real, rotated_c.imag)
