import random

random.seed(3)
a = random.random( )
random.seed(3)
b = random.random( )

print("seed(3) ")
print("a : ", a)
print("b : ", b)

random.seed( )
c = random.random( )
random.seed( )
d = random.random( )

print("seed() ")
print("c : ", c)
print("d : ", d)