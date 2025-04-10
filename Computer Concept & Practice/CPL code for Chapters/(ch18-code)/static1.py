class Fraction(object):
    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.simplify()
        
    def simplify(self):
        g = Fraction.gcd(self.num, self.den)
        self.num = self.num // g
        self.den = self.den // g
    
    @staticmethod
    def gcd(a, b):
        while b != 0:
            (a, b) = (b, a % b)
        return a
        