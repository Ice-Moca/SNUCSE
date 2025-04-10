import random

a = 'abcdefghij'
b = [1,2,3,4,5,6,7]
random.shuffle(b)
c = [1,2,3,4,5]

print("choice(a) : ",      random.choice(a) )
print("shuffle(b) : ", b)
print("sample(c, 3) : ", random.sample(c,3) )