# Determinism: input --> predictable output
# we want unpredictable outcomes
# The word Randomness means unpredictability
'''
Unbaised : no loaded dice
INformation-dense : high entropy
Incompressible : no short description of what comes next
'''

#a=1, c=7, m=12
current_x=0
def prng_seed(s):
    global current_x
    current_x=s

def LCG(n):
    return (n+7)%12

def prng():
    global current_x
    current_x=LCG(current_x)
    return current_x

#global: 전역변수 : 외부에서 변수 가지고 온다 여기서는 current_x
prng_seed(10)                           #초기값
print([prng() for i in range(20) ])     #12로 나누는 것 반복 --> 주기: 12


# c와 m의 최대 공약수가 1이여야한다.
# X=(aX+c)%m
# Max prtiod is m
# a-1은 m의 모든 소수인 약수로 나뉜다.
# m이 4의 배수라면 a-1 또한 4의 배수이다.
'''
import random 

random.seed(2)
#random generator by a=2

random.seed()
#random generator with current time

a=random.random()
#0<=x<1사이의 x를 return

random.uniform(a,b)
#a<=x<=b사이의 x를 return
 
random.randint(a,b)
#a<=x<=b사이의 정수 n을 return

random.randrange(a)
#0<=x<a사이의 정수 n을 return

random.randrange(a,b,c)
#a<=x<b사이의 정수 n=a+k*c를 return

random.choice(temp)
#temp의 원소중 하나를 return

random.shuffle(a)
#a를 전부 섞어서 return

random.sample(a,b)
#a중 b개를 리턴 return

'''
a='abcdef'
b=[1,2,3,4,5,6,7,8,9]
c=[1,5,4,3,2,1,4,3,2,1]

import random

print(random.choice(a))
random.shuffle(b)
print(b)
# random.shuffle(b)는 값이 아니라 포인터로 None이라고 나온다.

def random_pop(data):
    n=random.randint(0,len(data)-1)
    return data.pop(n)

if __name__=='__main__':
    data=[1,2,3,4,5]
    while data:
        print(random_pop(data))

#모든 데이터가 랜덤하게 튀어나온다.

'''
def random_pop_ver2(data):
    n=random.choice(data)
    data.remove(n)
    return n
    
if __name__=='__main__':
    while data:
        data=[1,2,3,4,5]
        print(random_pop_ver2(data))
'''

#set의 pop()과 같이 랜덤하게 작동할 수 있도록 list로 만든 것임