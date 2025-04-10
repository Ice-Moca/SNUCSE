class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __del__(self):
        print('Point destroyed')

pt1 = Point()
pt2 = pt1
pt3 = pt1
# prints the ids of the objects
print( id(pt1), id(pt2), id(pt3) ) 
del pt1
del pt2
del pt3