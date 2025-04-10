class Person:
    def __init__(self, name):
        self.name = name
        print(self.name)
    def Sayhello(self):
        print('Hello, my name is', self.name)
    def __del__(self):
        print('%s says bye.' % self.name)
    
A = Person('Yan Li')