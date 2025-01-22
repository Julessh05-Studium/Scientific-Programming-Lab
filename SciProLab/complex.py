from math import atan2, cos, sin, sqrt

from errors.ComplexZeroError import ComplexZeroError

# represents a complex number in the format
# of a + b * i or shortened: a + bi, which a being the
# real part and b the imaginary part of the complex number
class ComplexNumber:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def to_polar(self) -> 'PolarComplexNumber':
        if self.real == 0:
            raise ComplexZeroError
        else:
            r = sqrt(self.real**2 + self.imag**2)
            phi = atan2(self.imag, self.real)
            return PolarComplexNumber(r, phi)

    def __str__(self):
        return f"ComplexNumber({self.real} + {self.imag}i)\nnumber: {self.real} + {self.imag}i"

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)


class PolarComplexNumber:

    def __init__(self, r, phi):
        self.r = r
        self.phi = phi

    def __str__(self):
        return f"PolarComplexNumber({self.r}, {self.phi})\nnumber: {self.r} + e^({self.phi}i)"

    def to_cartesian(self) -> 'ComplexNumber':
        return ComplexNumber(self.r * cos(self.phi), self.r * sin(self.phi))