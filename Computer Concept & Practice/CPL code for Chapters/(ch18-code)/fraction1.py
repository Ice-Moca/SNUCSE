
class Fraction(object):
    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.simplify()
        
    def toString(self):
        return str(self.num) + "/" + str(self.den)
    
    def add(self, other):
        self.num1 = self.num * other.den
        other.num1 = other.num * self.den
        return Fraction(self.num1 + other.num1, self.den * other.den)

    def mul(self, other):
        ...
    def toFloat(self):
        ...
    def simplify(Self):
        ...

f1 = Fraction(4, 6)
f2 = Fraction(5, 9)
print(f1)        # <__main__.Fraction object at 0x1010349b0>
print(f1.toString())             # 2/3
print(f1.add(f2).toString())