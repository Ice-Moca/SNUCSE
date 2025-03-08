#Boolean 진리값 자료형
'''
print(5>10)
print(not 5>10)
print(10>5)

x and y     # if x==False: return False else: return y
x or y      # if x==True: return True else: return y

# order of operators : not > and > or
# a or not b and c == a or ((not b) and c)
'''

# 32bit maschine에서 정수 범위 -2**31 ~ 2**31
# 부호 비포함이면 0부터 2**32-1까지 정수가 표현된다. 
# 범위를 넘어가면 Python에서 bignum으로 자동연산된다.
'''
고정 소수점 방식 vs 부동 소수점 방식
1 15 16 (부 지 가)
1 8 23  (부 지 가)
# 부호부 지수부 가수부 (2진수 기준이다.)
'''