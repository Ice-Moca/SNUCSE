class Person:
    def speak(self):
        print('I can speak')
class Man(Person):
    def wear(self):
        print('I wear shirt')

class Woman(Person):
    def wear(self):
        print('I wear skirt')

man = Man()
print( man.wear() )   # I wear shirt
print( man.speak() )  # I can speak