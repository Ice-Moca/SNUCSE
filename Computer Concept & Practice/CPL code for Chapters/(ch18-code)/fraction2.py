
class Fraction(object):
    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.simplify()

    def simplify(self):
        g = gcd(self.num, self.den)
        self.num = self.num // g
        self.den = self.den // g

    def __str__ (self):
        return str(self.num) + "/" + str(self.den)

    def __repr__(self):
        return str(self.num / self.den)

    def __add__ (self, other):
        self.num1 = self.num * other.den
        other.num1 = other.num * self.den
        return Fraction(self.num1 + other.num1, self.den * other.den)

    def __hash__(self):
      hashables = (self.num, self.den)
      return hash(hashables)

def gcd(a, b):
        while b != 0:
            (a, b) = (b, a % b)
        return a
        


f1 = Fraction(4, 6)
f2 = Fraction(5, 9)
print( f1 )        # 2/3  
print( f1 + f2 )   # 11/9