# 변수 (Variable)는 메모리에 데이터를 저장하는데 사용되는 공간의 이름이다.

# 선언과 할당
age = 10

print(age)
print(type(age))

# 10
# <class 'int'>

# age라는 변수에 숫자 10을 할당했다.

# 파이썬에서는 변수의 자료형을 따로 지정해주지 않아도 값에 따라 자동으로 결정되는데, 
# 파이썬 내장함수 type()을 이용해서 변수의 자료형을 확인해보면 int 형인 것을 알 수 있다. 

# 새로운 값 할당하기
age = 10
print(age) # 10

age += 1 
print(age) # 11

# 코드 안에서 새로운 값이 할당되지 않는 동안 변수의 값은 그대로 유지된다.
# 할당 연산자 +=를 이용해서 변수에 1을 더해주면, 이제 변수의 값은 11이 된다. 

# 다양한 자료형
age = 11
deposit = -33000
ratio = 1.5
fruit = 'apple'

print(age, type(age))            # 11 <class 'int'>
print(deposit, type(deposit))    # -33000 <class 'int'>
print(ratio, type(ratio))        # 1.5 <class 'float'>
print(fruit, type(fruit))        # apple <class 'str'>

# 변수에는 정수, 실수, 문자열 등 다양한 값을 할당할 수 있다. 
# 자료형을 확인해보면, 각각 int, float, str 형임을 알 수 있다.


# 문자열 연결
age = 11 + 1
fruit = 'pine' + 'apple'

print(age)
print(fruit)

# 숫자끼리 더하면 값이 더해지고,
# 문자열을 더하면 문자열이 연결된다.
# 파이썬의 이러한 기능을 문자열 연결 (string concatenation)이라고 한다.

# 동시에 선언, 할당하기
a = b = c = 10
d, e, f = 10, 35.2, 'pineapple'

# 동일한 값을 갖는 변수를 동시에 선언할 수도 있고,
# 각각 다른 값을 동시에 할당할 수도 있다.


# 변수 이름 정하기

# 1. 의미를 알 수 있게 하자.
a = 10               # Bad
age = 10             # Good

# 예를 들어, 나이를 나타내는 변수의 이름은 ‘a’ 대신 ‘age’로 하는 것이 좋다.


# 2. 소문자 ‘l’/대문자 ‘O’/대문자 ‘I’는 피하자.
l = '1ong'           # Bad!
O = '0range'         # Bad!
I = 'line'           # Bad!

# 소문자 l은 숫자 1과 구분하기 어려울 수 있다.
# 대문자 O는 숫자 0과 구분하기 어려울 수 있다.
# 대문자 I는 소문자 l과 구분하기 어려울 수 있다.


# 3. 변수와 함수의 이름은 소문자로.

def hello():
   print('Hello')

hello()
# 변수와 함수의 이름은 기본적으로 소문자로 지정한다.


# 4. 문자열의 연결은 언더스코어 (_)을 사용하자.
# 가독성을 높이기 위해서 단어 간의 연결은 언더스코어 (_)를 사용한다.

# 함수
def say_hello():
   print('Hello')


say_hello()

# 변수
fruitsnumber = 20    # Bad
num_fruits = 20      # Good


# 5. 클래스의 이름은 CapWords 스타일로.
class MemberInfo():
   pass

# 클래스의 이름을 정할 때에는 CapWords와 같이 단어의 첫 글자에만 대문자를 사용한다.

# 6. 상수는 모두 대문자로.
PI = 3.14
TEMP = 300

# 파이썬에서 사용하는 상수에는 모두 대문자를 사용한다.