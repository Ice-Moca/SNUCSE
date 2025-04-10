class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    
a = FourCal(4, 2)
b = FourCal(3, 7)

a.sum() # 6
a.mul() # 8
a.sub() # 2
a.div() # 2
b.sum() # 10
b.mul() # 21
b.sub() # -4
b.div() # 0