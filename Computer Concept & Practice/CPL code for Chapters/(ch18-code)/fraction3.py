class Fraction(object):
    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.simplify()

    def simplify(self):
        g = gcd(self.num, self.den)
        self.num = self.num // g
        self.den = self.den // g

    def __str__ (self):             #string representation
        return str(self.num) + "/" + str(self.den)

    def __repr__(self):             #offcial representation : print()는 __str__()가 없으면 __repr__()를 call한다
        return str(self.num) + "/" + str(self.den)

    def __add__ (self, other):
        self.num1 = self.num * other.den
        other.num1 = other.num * self.den
        return Fraction(self.num1 + other.num1, self.den * other.den)

def gcd(a, b):
        while b != 0:
            (a, b) = (b, a % b)
        return a
