'''
import numpy as np

v1=np.array([2,5])
v2=np.array([3,10])

v1+v2               # array([5,15])
print(v1+v2)        # [5 15] 라는 결과값이 나옴
'''

class Vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def __str__(self):                                      # 문자열을 출력하는 것처럼 print()안에 넣을 수 있도록하는 방법
        return 'Vector(%d, %d)' %(self.a,self.b)
    
    def __add__(self,other):
        return Vector(self.a+ other.a, self.b+ other.b)
    
v1=Vector(2,10)
v2=Vector(5,-2)
print(v1+v2)