class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
    def eat(self, food):
        if food == 'apple':
            self.health =  self.health -  100
        elif food == 'ham':
            self.health =  self.health + 20

BBB = Hero("Bob")
print(BBB.name)
print(BBB.health)
BBB.eat("ham")
print(BBB.health)