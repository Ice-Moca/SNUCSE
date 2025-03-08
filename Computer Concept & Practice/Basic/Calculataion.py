# Python 연산자 (Operators)

# 연산자 (Operator)는 산술, 논리 연산 등을 수행하기 위한 특수 기호를 말한다.
# 연산자가 연산을 수행하는 값 또는 데이터를 피연산자 (operand)라고 한다.

# 예를 들어, 더하기 연산를 수행하는 산술 연산자 + 에 대해, 1과 2는 피연산자이고,
# 3은 연산의 결과값이다.

 
# 연산자와 피연산자.
# 아래에서 파이썬에서 사용할 수 있는 다양한 연산자에 대해 소개한다.


# 산술 연산자 (Arithmetic operator)
# 산술 연산자 (Arithmetic operator)는 더하기, 빼기, 곱하기, 나누기 등과 같은 수학 연산을 수행하는데 사용된다.  

'''
산술 연산자 종류

+   :   두 피연산자를 더하거나 (add), 단항 더하기 (unary plus) 연산을 수행한다.

-   :   두 피연산자를 빼거나 (subtract), 단항 빼기 (unary minus) 연산을 수행한다.

*   :   두 피연산자를 곱한다.

/   :   왼쪽 피연산자를 오른쪽 피연산자로 나눈다. (결과는 항상 float)

%   :   모듈러스(mod). 왼쪽 피연산자를 오른쪽 피연산자로 나눈 나머지.

//   :   버림 나눗셈 (floor division).

**   :   지수 (exponent) 연산.
'''

# 예제
print(3 + 2)        # Result: 5

print(3 - 2)        # Result: 1

print(3 * 2)        # Result: 6

print(3 / 2)        # Result: 1.5
print(10 / -3)      # Result: -3.3333333333333335
print(6 / 2)        # Result: 3.0

print(3 // 2)       # Result: 1
print(10 // -3)     # Result: -4

print(3 ** 2)       # Result: 9

# 나누기 연산에 대해 결과는 항상 실수형 (float)이 됩니다.



# 비교 연산자 (Comparison operator)
# 비교 연산자 (Comparison operator)는 값을 비교하는데 사용된다.
# 조건에 따라 True 또는 False를 반환한다.

'''
비교 연산자 종류

>   :   왼쪽 피연산자가 오른쪽 피연산자보다 크다.

<   :   왼쪽 피연산자가 오른쪽 피연산자보다 작다.

==   :   두 피연산자가 같다.

!=   :   두 피연산자가 같지 않다.

>=   :   왼쪽 피연산자가 오른쪽 피연산자보다 크거나 같다.

<=   :   왼쪽 피연산자가 오른쪽 피연산자보다 작거나 같다.
'''

# 예제
print(3 > 2)         # Result: True

print(3 < 2)         # Result: False

print(2 == 2)        # Result: True
print(2 == 2.0)      # Result: True

print(3 != 2)        # Result: True

print(2 >= 5)        # Result: False

print(2 <= 5)        # Result: True

# 연산의 결과가 참일 경우 True를, 그렇지 않은 경우 False를 출력합니다.
# 이를 중첩하여 연속으로 사용할 수 있다.
# Ex) print(2<3<=5)


# 논리 연산자 (Logic operator)
# 논리 연산자 (Logic operator)는 and, or, not이다.

'''
논리 연산자 종류

and   :   두 피연산자가 모두 참일 때, True.

or   :   두 피연산자 중 하나가 참일 때, True.  

not   :   피연산자가 참이면, False, 거짓이면 True.
'''
# or의 경우 |와 연산이 다르다.

# 예제
a = True
b = False

print(a and b)       # Result: False
print(a or b)        # Result: True
print(not a)         # Result: False
print(not b)         # Result: True

# 두 피연산자 a, b의 참, 거짓 여부에 따라 and, or, not 연산의 결과를 출력한다.


# 할당 연산자 (Assignment operator)
# 할당 연산자 (Assignment operator)는 변수 (variable)에 값을 할당할 때 사용한다.  

'''
할당 연산자 종류
=   :   변수에 값을 할당한다.
+=   :   변수에 값을 더한 결과를 할당한다.
-=   :   변수에 값을 뺀 결과를 할당한다.
*=   :   변수에 값을 곱한 결과를 할당한다.
/=   :   변수에 값을 나눈 결과를 할당한다.
%=   :   변수를 값으로 나눈 나머지를 할당한다.
//=   :   변수를 값으로 나눈 몫 (floor division)을 할당한다.
**=   :   변수를 값으로 제곱한 결과를 할당한다.
'''

# While, for loop문에서 자주 사용하므로 기억해두자

# 예제
x = 3
x += 3          # x = x + 3
x -= 3          # x = x - 3
x *= 3          # x = x * 3
x /= 3          # x = x / 3
x %= 3          # x = x % 3
x //= 3         # x = x // 3
x **= 3         # x = x ** 3

# 특수 연산자 (Special operator)
# 파이썬은 식별 연산자 (identity operator)와 멤버 연산자 (membership operator)와 같은 특수 연산자 (special operator)를 제공한다.

'''
식별 연산자 종류
식별 연산자는 두 값 또는 변수가 동일한 객체인지 확인하는데 사용된다.

is   :   두 연산자가 동일하면 True.
is not   :   두 연산자가 동일하지 않으면 True. 
'''

# 예제
x1 = 5
y1 = 5

print(x1 is y1)         # Result: True

x2 = 'Hello'
y2 = 'Hello'
z2 = 'hello'

print(x2 is not y2)     # Result: False
print(x2 is not z2)     # Result: True

# x1과 y1이 같으므로 x1 is y1는 참이 된다.
# x2와 y2는 같으므로 x2 is not y2는 거짓이 된다.
# x2와 z2는 같지 않으므로 x2 is not z2는 참이 된다.

'''
멤버 연산자 종류
멤버 연산자는 값 또는 변수가 문자열, 리스트, 튜플, 집합, 딕셔너리 등에 포함되어 있는지 확인하는데 사용된다.

in   :   값 또는 변수가 포함되어 있으면 True.

not in   :   값 또는 변수가 포함되어 있지 않으면 True.
'''

# 예제
x = 'Python'

print('p' in x)         # Result: False
print('y' in x)         # Result: True

y = [1, 3, 2, 5]

print(1 in y)           # Result: True
print(4 in y)           # Result: False

# 문자 ‘p’가 ‘Python’에 포함되어 있지 않으므로, 'p' in x는 거짓이 된다.
# 문자 ‘y’가 ‘Python’에 포함되어 있으므로, 'y' in x는 참이 된다.
# 정수 1이 리스트 [1, 3, 2, 5]에 포함되어 있으므로, 1 in y는 참이 된다.
# 정수 4가 리스트 [1, 3, 2, 5]에 포함되어 있지 않으므로, 4 in y는 거짓이 된다.


