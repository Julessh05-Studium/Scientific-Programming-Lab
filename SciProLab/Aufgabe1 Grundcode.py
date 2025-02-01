import math




class ComplexNumberError(Exception):
    pass


class ComplexNumber:
    
    def __init__(self, real, imag):
        if not isinstance(real, (int, float)) or not isinstance(imag, (int, float)):
            raise TypeError("Die Eingabewerte müssen Zahlen (int oder float) sein.")
        self.real = real
        self.imag = imag

    def __repr__(self):
            return f"ComplexNumber({self.real}, {self.imag})"
            
    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"

    def get_real(self):
        return self.real
    
    def get_imag(self):
        return self.imag
        
    def __add__(self, other):
        if type(other) in (int,float):
            new_real = self.real + other
            new_imag = self.imag
            return ComplexNumber(new_real, new_imag)
        elif type(other) == ComplexNumber:
            new_real = self.real + other.real
            new_imag = self.imag + other.imag
            return ComplexNumber(new_real, new_imag)
        else:
            raise TypeError

    def __sub__(self, other):
        if type(other) in (int,float):
            new_real = self.real - other
            new_imag = self.imag
            return ComplexNumber(new_real, new_imag)
        elif type(other) == ComplexNumber:
            new_real = self.real - other.real
            new_imag = self.imag - other.imag
            return ComplexNumber(new_real, new_imag)
        else:
            raise TypeError

    def __mul__(self,other):
        if type(other) in (int,float):
            new_real = self.real * other
            new_imag = self.imag * other
            return ComplexNumber(new_real, new_imag)
        elif type(other) == ComplexNumber:
            new_real = self.real * other.real - self.imag * other.imag
            new_imag = self.real * other.imag + self.imag * other.real
            return ComplexNumber(new_real, new_imag)
        else:
            raise TypeError

    def __truediv__(self,other):
        if type(other) in (int,float):
            new_real = self.real / other
            new_imag = self.imag / other
            return ComplexNumber(new_real, new_imag)
        elif type(other) == ComplexNumber:
            if other.real == 0 and other.imag == 0:
                raise ComplexNumberError("Division durch Null ist nicht definiert für komplexe Zahlen.")
            div = other.real**2 + other.imag**2
            new_real = (self.real * other.real + self.imag * other.imag) / div
            new_imag = (self.imag * other.real - self.real * other.imag) / div
            return ComplexNumber(new_real, new_imag)
        else:
            raise TypeError

    def __radd__(self,other):
        return self.__add__(other)
        
    def __rsub__(self,other):
        if type(other) in (float,int):
            return ComplexNumber(other-self.real,-self.imag)
        else:
            raise TypeError
        
    def __rmul__(self,other):
        return self * other
        # return self.__mul____(other)
        
    def __rtruediv__(self,other):
        if type(other) in (int,float):
            return ComplexNumber(other,0) / self
        else:
            raise TypeError
        

    def __eq__(self,other):
        return self.real == other.real and self.imag == other.imag
    """def __eq__(self, other):
        tolerance = 1e-14  # Toleranzbereich für den Vergleich
        return abs(self.real - other.real) < tolerance and abs(self.imag - other.imag) < tolerance  """  
        
    def is_real(self):
        return self.imag == 0

    def __pow__(self, power):
        """Potenzieren einer komplexen Zahl"""
        r, theta = self.to_polar()  # Umrechnung in Polarform
        r_new = r ** power
        theta_new = theta * power
        return self.to_kart(r_new, theta_new)    
        
    def to_real(self):
        "Prüft, ob die Zahl reell ist und gibt sie als reelle Zahl zurück"
        if self.imag == 0:
            return self.real
        else:
            return self
                
    def to_polar(self):
        "Umrechnung von kartesischen Koordinaten (Real, Imaginär) in Polarkoordinaten (r, theta)"
        r = math.sqrt(self.real**2 + self.imag**2)
        theta = math.atan2(self.imag, self.real)
        return r, theta

    def to_kart(self, r, theta):
        """Umrechnung von Polarkoordinaten (r, theta) in kartesische Koordinaten (Real, Imaginär)"""
        real = r * math.cos(theta)
        imag = r * math.sin(theta)
        return ComplexNumber(real, imag)   
            
    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def to_tuple(self):
        return (self.real, self.imag)
