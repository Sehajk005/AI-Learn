class Fractions:
    
    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d
        
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    # fraction: "{}/{}".format(self.numerator, self.denominator)
    
    def __add__(self, other):
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fractions(new_numerator, new_denominator)
    
    def __sub__(self, other):
        new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fractions(new_numerator, new_denominator)
    
    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fractions(new_numerator, new_denominator)
    
    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fractions(new_numerator, new_denominator)
    
fraction1 = Fractions(3, 4)
fraction2 = Fractions(5, 6)
print(fraction1 + fraction2)
print(fraction1 - fraction2)
print(fraction1 * fraction2)
print(fraction1 / fraction2)