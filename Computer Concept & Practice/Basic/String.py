#String 문자열 자료형
# 문자열 (String)은 하나 이상 연속된 문자 (character)들의 나열입니다.
# 파이썬에서 문자열 자료형은 큰따옴표 (” “) 또는 작은따옴표 (‘ ‘) 사이에 위치합니다.
#immutable한 자료이다. 하지만 replace()로는 교체 가능


print("\"헛소리하지마 임마!\"") 
# 따옴표를 작성하고 싶을때는 "\'" 꼴로 표시한다.


Time= 4
print('For %d times what have you done?' %Time)
# %d, %f, %c등을 이용하여 c++이나 C처럼 코딩가능하다.


# 예제1
string1 = "apple"
string2 = 'banana'

print(string1)  # apple
print(string2)  # banana

# 문자열 “apple”과 ‘banana’를 각각 string1, string2에 할당하고 출력했습니다.

# 예제2
string3 = "'orange'"
string4 = '"mango"'

print(string3)  # 'orange'
print(string4)  # "mango"

# 큰따옴표와 작은따옴표를 사용하는 것에 차이는 없지만 위의 예제와 같이 두 종류의 따옴표를 사용해서 따옴표를 그대로 출력할 수도 있습니다.

# 예제3
string5 = """Courage is very important.
Like a muscle,
it is strengthened by use."""

string6 = '''By doubting
            we come at the truth.'''

print(string5, '\n') 
print(string6)

# 따옴표 세 개를 사용하면 여러줄의 문자열을 사용할 수 있습니다. 



# 문자열 인덱싱
# 리스트, 튜플과 마찬가지로 문자열에서도 인덱스를 사용할 수 있습니다.
string7 = 'Good Morning!'

print(string7[0])
print(string7[3])
print(string7[4])
print(string7[-1])

# 다섯번째 문자인 string7[4]는 공백 (‘ ‘)입니다.
# 마지막 문자 (‘!’)는 string7[-1]와 같이 음의 인덱스를 사용해서 편리하게 접근할 수 있습니다.


# 문자열 슬라이싱
# 또한 리스트, 튜플과 마찬가지로 문자열에 대해서도 슬라이싱 기능을 사용할 수 있습니다.
string8 = 'Good Evening!'

print(string8[2:7])
print(string8[:4])
print(string8[5:])

# string8[2:7]은 세번째부터 일곱번째 문자를 슬라이스합니다.
# string8[:4]은 처음부터 네번째 문자를 슬라이스합니다.
# string8[5:]은 여섯번째부터 마지막 문자까지 슬라이스합니다.


# 문자열 연결하기
# 파이썬에서는 더하기 연산자를 이용해서 문자열을 연결할 수 있습니다.
string9 = 'Good'
string10 = 'Evening!'

print(string9 + string10)
print(string9 + ' ' + string10)
print(string9, string10)

# string9 + string10은 ‘Good’와 ‘Evening!’를 연결한 문자열입니다.
# 두 문자열의 가운데에 공백을 삽입해서 ‘Good Evening!’을 출력했습니다.



# 문자열 루프 (Loop)
# 문자열를 이터레이트 (iterate)하기 위해 아래와 같이 for 루프를 사용할 수 있습니다.
string11 = 'Python String'

for c in string11:
  print(c)


# 문자열 포함 여부 확인하기
# 파이썬 키워드 in과 not을 사용하면, 문자열이 특정 문자 또는 문자열을 포함하는지 여부를 간단하게 확인할 수 있습니다.

string12 = 'codetorial.net'

print('code' in string12)
print('real' in string12)
print('.' not in string12)

# 문자열 ‘codetorial.net’은 문자열 ‘code’와 문자 ‘.’를 포함하고,
# 문자열 ‘real’을 포함하지 않습니다.


'''
문자열 메서드
파이썬에서는 문자열과 함께 사용할 수 있는 다양한 메서드를 제공합니다.
주요한 문자열 메서드를 간단한 예제와 함께 소개합니다.
'''

'''
# count()
# 문자열 안에서 입력한 문자가 나타나는 횟수를 반환합니다.
a = 'banana'

print(a.count('a'))
# 3

# join()
# 반복 가능한 객체 (리스트, 튜플 등)를 문자열을 사용해서 연결합니다.
fruits = ['apple', 'banana', 'orange']

print(', '.join(fruits))
# apple, banana, orange


# rsplit()
# (문자열의 뒤에서부터) 입력한 문자(열)를 기준으로 문자열을 쪼개서 리스트의 형태로 반환합니다.
# maxsplit를 입력하면 문자열을 쪼개는 최대 횟수를 지정합니다.
a = 'apple, banana, orange'

print(a.rsplit(', '))
print(a.rsplit(', ', 1))
# ['apple', 'banana', 'orange']
# ['apple, banana', 'orange']

# split()
# (문자열의 앞에서부터) 입력한 문자(열)를 기준으로 문자열을 쪼개서 리스트의 형태로 반환합니다.
# maxsplit를 입력하면 문자열을 쪼개는 최대 횟수를 지정합니다.
a = 'apple, banana, orange'

print(a.split(', '))
print(a.split(', ', 1))
# ['apple', 'banana', 'orange']
# ['apple', 'banana, orange']
'''

# lower()
# 문자열을 소문자로 변환합니다.
a = 'Python'

print(a.lower())
# python

# replace()
# 문자열의 특정 문자를 다른 문자로 치환합니다.
a = 'banana'

print(a.replace('a', 'o'))
print(a)
# bonono
# banana 따라서 이는 a가 바뀐 것이 아닌 새로운 문자열을 만든 함수임을 알 수 있다.

# find()
# 문자열의 앞에서부터 입력한 문자(열)를 검색해서 인덱스를 반환합니다.
# 문자 또는 문자열이 없다면 -1를 반환합니다.
a = 'banana'

print(a.find('a'))
print(a.find('d'))
# 1
# -1


# index()
# find() 메서드와 마찬가지로 입력한 문자(열)의 인덱스를 반환합니다.
# find() 메서드와 달리 문자 또는 문자열을 찾지 못했을 때 에러를 발생합니다.
a = 'banana'

print(a.index('a'))
print(a.index('d'))
# 1
# Traceback (most recent call last):
#   File "/Users/python/test.py", line 3, in <module>
#     print(a.index('d'))
# ValueError: substring not found


# strip()
# 앞뒤 공백을 제거한 문자열을 반환합니다.
# 문자열 사이의 공백은 제거하지 않습니다.
a = '  Python  '
b = '  Just Do It!'

print(a.strip())
print(b.strip())
# Python
# Just Do It!

'''
isalnum()
문자열이 알파벳 (A-Z, a-z) 또는 숫자 (0-9)로 이루어져 있다면 True, 그렇지 않다면 False를 반환합니다.
a = 'ABC123'
b = 'abc123!'

print(a.isalnum())
print(b.isalnum())
True
False

isalpha()
문자열이 알파벳 (A-Z, a-z)으로 이루어져 있다면 True, 그렇지 않다면 False를 반환합니다.
a = 'ABC'
b = '123!'

print(a.isalpha())
print(b.isalpha())
True
False

isdecimal()
문자열이 십진수 (decimal)로 이루어져 있다면 True, 그렇지 않다면 False를 반환합니다.
a = '10'
b = '0b1010'
c = str(int(b, 2))

print(a, a.isdecimal())
print(b, b.isdecimal())
print(c, c.isdecimal())
10 True
0b1010 False
10 True

islower()
문자열이 모두 소문자로 이루어져 있다면 True, 그렇지 않다면 False를 반환합니다.
a = 'python'
b = 'Python'

print(a.islower())
print(b.islower())
True
False

isspace()
문자열이 모두 공백으로 이루어져 있다면 True, 그렇지 않다면 False를 반환합니다.
a = 'a b c'
b = 'a   c'
c = '     '

print(a.isspace())
print(b.isspace())
print(c.isspace())
False
False
True

isupper()
모든 문자열이 대문자라면 True, 그렇지 않다면 False를 반환합니다.
a = 'python'
b = 'Python'
c = 'PYTHON'

print(a.isupper())
print(b.isupper())
print(c.isupper())
False
False
True

'''
# rfind()
# 문자열의 뒤에서부터 입력한 문자(열)를 검색해서 인덱스를 반환합니다.
# 문자 또는 문자열이 없다면 -1를 반환합니다.
a = 'banana'

print(a.rfind('a'))
print(a.rfind('d'))
# 5
# -1


# capitalize()
# 문자열의 첫번째 문자를 대문자로 변환합니다.
a = 'python'

print(a.capitalize())
# Python

# casefold()
# 문자열을 소문자로 변환합니다.

a = 'Python'
b = 'PYTHON'
print(a.casefold()) # python
print(b.casefold()) # python


# center()
# 문자열을 가운데 정렬합니다.
# 문자를 입력하면 공백을 문자로 채웁니다.

a = 'Python'
print(a.center(16, '-'))
# -----Python-----


# endswith()
# 문자열이 입력한 문자(열)로 끝난다면 True를 반환하고, 그렇지 않다면 False를 반환합니다.
# a = 'codetorial.net'

# print(a.endswith('net'))
# True


# startswith()
# 문자열이 입력한 문자(열)로 시작한다면 True를 반환하고, 그렇지 않다면 False를 반환합니다.
# a = 'codetorial.net'

# print(a.startswith('code'))
# True


# swapcase()
# 대문자를 소문자로, 소문자를 대문자로 변환한 문자열을 반환합니다.
# a = 'Python'

# print(a.swapcase())
# pYTHON

# title()
# 첫번째 문자를 대문자로 변환한 ‘제목’ 스타일의 문자열을 반환합니다.
# a = 'just do it!'

# print(a.title())
# Just Do It!

# upper()
# 문자열을 대문자로 변환합니다.
# a = 'Python'

# print(a.upper())
# PYTHON

# zfill()
# 문자열 앞에 숫자 0을 채워서 입력한 숫자만큼의 길이가 되도록 합니다.
# a = '15'
# b = '2416'

# print(a.zfill(6))
# print(b.zfill(6))
# 000015
