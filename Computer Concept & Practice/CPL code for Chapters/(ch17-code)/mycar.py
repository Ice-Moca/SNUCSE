class Automobile(object):
    def __init__(self, width, height, length):
        self.width = width
        self.height = height
        self.length = length
        print("A new Automobile instance is allocated")
    def compute_volume(self):
        return self.width * self.height * self.length

class Pickup_Truck(Automobile):
    def __init__(self, width, height, length, loading_area):
        Automobile.__init__(self, width, height, length)
        self.loading_area = loading_area
    def compute_volume_1(self):
        return self.width * self.height * self.length + self.loading_area

def test():
    mycar = Automobile(10, 15, 25)
    print("Mycar\'s volume is", mycar.compute_volume())
    yourcar = Pickup_Truck(10, 15, 25, 1000)
    print("Yourcar\'s volume is", yourcar.compute_volume())
    print("Yourcar \'s volume with loading section is", yourcar.compute_volume_1())

test()