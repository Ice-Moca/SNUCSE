set_fruit = {'apple', 'banana', 'orange'}
print(set_fruit)

set_fruit2 = set([1, 2, 3, 4])
print(set_fruit2)

set_fruit3 = set('apple')
print(set_fruit3)
# {'orange', 'apple', 'banana'}
# {1, 2, 3, 4}
# {'a', 'p', 'e', 'l'}

# set(‘apple’)은 ‘apple’의 각각의 문자를 갖는 집합을 만드는데, 문자 ‘p’는 한 번만 포함됩니다.
# 빈 집합을 만들기 위해서는 {} 대신 set()를 사용합니다. {}을 사용하면 딕셔너리가 만들어집니다.


# 집합 요소 값 얻기
# 파이썬 리스트, 튜플, 딕셔너리와 달리 집합의 요소 값들은 직접 접근할 수 없습니다.
# 하지만 for 반복문을 이용해서 집합의 모든 값들을 얻을 수 있습니다.
set_fruit = {'apple', 'banana', 'orange'}

for fruit in set_fruit:
  print(fruit)
# banana
# apple
# orange


# 집합 값 추가하기
# 집합에 요소를 추가하기 위해서는 add() 또는 update() 메서드를 사용합니다.

# add() 
# 집합에 한 개의 값을 추가할 때 add() 메서드를 사용할 수 있습니다.
set_fruit = {'apple', 'banana', 'orange'}
print(set_fruit)

set_fruit.add('watermelon')
print(set_fruit)
{'apple', 'orange', 'banana'}
{'apple', 'orange', 'banana', 'watermelon'}
# ‘watermelon’ 요소가 집합에 추가됩니다.



# update()
# 집합에 여러 개의 요소를 추가하기 위해서 update() 메서드를 사용할 수 있습니다.
set_fruit = {'apple', 'banana', 'orange'}
print(set_fruit)

set_fruit.update(['watemelon', 'mango'])
print(set_fruit)
# {'orange', 'banana', 'apple'}
# {'banana', 'apple', 'mango', 'watemelon', 'orange'}




# 집합 값 삭제하기
# 집합의 요소를 삭제하기 위해서는 discard(), remove(), pop() 메서드를 사용합니다.

# discard()
set_fruit = {'apple', 'banana', 'orange'}
print(set_fruit)

set_fruit.discard('apple')
print(set_fruit)

set_fruit.discard('mango')
print(set_fruit)
{'orange', 'banana', 'apple'}
{'orange', 'banana'}
{'orange', 'banana'}
# 삭제할 요소가 없을 때는 집합에 변화가 생기지 않습니다.

# remove()
# remove() 메서드의 동작은 discard()와 유사하지만, 삭제할 요소가 없을 때 에러를 발생하는 점이 다릅니다.
set_fruit = {'apple', 'banana', 'orange'}
print(set_fruit)

set_fruit.remove('apple')
print(set_fruit)

set_fruit.remove('mango')
print(set_fruit)
# {'apple', 'orange', 'banana'}
# {'orange', 'banana'}
# Traceback (most recent call last):
# File "main.py", line 7, in <module>
#   set_fruit.remove('mango')
# KeyError: 'mango'

# pop()
# 집합에서 요소를 삭제하기 위해 pop() 메서드를 사용할 수도 있습니다.
# pop() 메서드는 보통 마지막 요소를 뽑아서 반환하는 동작을 하지만, 집합은 순서가 없기 때문에 어떤 요소가 반환될지 알 수 없습니다.
set_fruit = {'apple', 'banana', 'orange'}
print(set_fruit)

set_fruit.add('mango')
print(set_fruit)
print(set_fruit.pop())
print(set_fruit)
# {'orange', 'banana', 'apple'}
# {'orange', 'banana', 'apple', 'mango'}
# orange
# {'banana', 'apple', 'mango'}




# clear()
# clear() 메서드는 집합을 빈 집합으로 만듭니다.
set_fruit = {'apple', 'banana', 'orange'}
print(set_fruit)

set_fruit.clear()
print(set_fruit)
# {'orange', 'apple', 'banana'}
# set()



# 집합 제거하기
# del
# del 키워드를 사용해서 집합을 제거할 수 있습니다.
set_fruit = {'apple', 'banana', 'orange'}
print(set_fruit)

del set_fruit
print(set_fruit)
# {'apple', 'banana', 'orange'}
# Traceback (most recent call last):
#   File "main.py", line 5, in <module>
#     print(set_fruit)
# NameError: name 'set_fruit' is not defined

# set_fruit 집합을 제거했습니다.
# 제거할 집합이 없다면 에러를 발생합니다.


# 집합 연산
# 파이썬의 집합 자료형을 이용해서 합집합, 교집합, 차집합, 대칭차집합과 같은 수학적 집합 연산을 수행할 수 있습니다.
# 집합 연산을 위해 union(), intersection(), difference(), symmetric_difference()과 같은 다양한 메서드를 사용합니다.

# union() - 합집합
# 두 집합의 합집합을 얻기 위해 union() 메서드를 사용합니다.
set_A = {1, 2, 4, 7}
set_B = {2, 3, 7, 9}

print(set_A.union(set_B))
print(set_B.union(set_A))
print(set_A | set_B)
# {1, 2, 3, 4, 7, 9}
# {1, 2, 3, 4, 7, 9}
# {1, 2, 3, 4, 7, 9}

# | 연산자는 union() 메서드와 같은 동작을 구현합니다.


# intersection() - 교집합 
# 두 집합의 교집합을 얻기 위해 intersection() 메서드를 사용합니다.
set_A = {1, 2, 4, 7}
set_B = {2, 3, 7, 9}

print(set_A.intersection(set_B))
print(set_B.intersection(set_A))
print(set_A & set_B)
# {2, 7}
# {2, 7}
# {2, 7}
# & 연산자는 intersection() 메서드와 같은 동작을 구현합니다.


# difference() - 차집합
# 두 집합의 차집합을 얻기 위해 difference() 메서드를 사용합니다.
set_A = {1, 2, 4, 7}
set_B = {2, 3, 7, 9}

print(set_A.difference(set_B))
print(set_A - set_B)
print(set_B.difference(set_A))
print(set_B - set_A)
# {1, 4}
# {1, 4}
# {9, 3}
# {9, 3}
# - 연산자는 difference() 메서드와 같은 동작을 구현합니다.


# symmetric_difference() - 대칭차집합
# 두 집합의 대칭차집합을 얻기 위해 symmetric_difference() 메서드를 사용합니다.
set_A = {1, 2, 4, 7}
set_B = {2, 3, 7, 9}

print(set_A.symmetric_difference(set_B))
print(set_B.symmetric_difference(set_A))
print(set_A ^ set_B)
{1, 3, 4, 9}
{1, 3, 4, 9}
{1, 3, 4, 9}
# ^ 연산자는 symmetric_difference() 메서드와 같은 동작을 구현합니다.


'''
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''


# Tuple data type

# Python 튜플 (Tuple)
# 리스트, 튜플, 문자열은 파이썬의 기본적인 시퀀스 자료형입니다.
# 시퀀스 자료형은 인덱싱, 슬라이싱, 반복 등의 연산을 수행할 수 있고, 파이썬의 내장함수 len()을 사용하면 그 크기를 확인할 수 있습니다.

# 튜플 (Tuple)은 소괄호 사이에 콤마로 구분되는 값들의 목록입니다.
# 리스트와 마찬가지로 다양한 자료형을 포함할 수 있지만, 한 번 만들어지면 새로운 값을 할당할 수 없다는 차이가 있습니다. 
 
# 이 페이지에서는 파이썬에서 튜플을 사용하는 방법에 대해 알아봅니다.

# 튜플 만들기
nums1 = (1, 2, 3)
nums2 = 1, 2, 3
vals = ('apple', 1, True)
nested = ([1, 2], (3, 4, 5), 'banana')

print(nums1)
print(nums2)
print(vals)
# (1, 2, 3)
# (1, 2, 3)
# ('apple', 1, True)
# ([1, 2], (3, 4, 5), 'banana')

# nums1과 같이 튜플은 괄호 안에 콤마로 값들을 연결함으로써 만들 수 있습니다.
# 또한 nums2와 같이 괄호를 사용하지 않아도 콤마로 연결된 값들은 튜플이 됩니다.
# 튜플의 값들이 꼭 같은 자료형일 필요는 없습니다. 문자열, 숫자, 불 값 등 여러 자료형을 포함할 수 있습니다.
# 또한 리스트나, 또 다른 튜플을 포함할 수도 있습니다.

# 튜플 인덱싱
nums = (1, 2, 3, 4, 5)

print(nums[1])
print(nums[3])
print(nums[-1])
print(nums[-5])
# 2
# 4
# 5
# 1
# 리스트와 마찬가지로 양 또는 음의 인덱스를 이용해서 튜플의 값에 접근할 수 있습니다.
# -1 인덱스를 사용해서 튜플의 맨 마지막 값에 쉽게 접근할 수 있습니다.
# 튜플의 인덱싱에 대해서 아래의 그림을 참고하세요.
 

# 튜플 슬라이싱
nums = (1, 2, 3, 4, 5)

print(nums[1:4])
print(nums[-4:-2])
print(nums[::2])
print(nums[::-2])
# (2, 3, 4)
# (2, 3)
# (1, 3, 5)
# (5, 3, 1)

# 또한 리스트와 마찬가지로 튜플의 일부 구간 또는 값을 가져오고 싶을 때 슬라이싱을 사용할 수 있습니다.

# 콜론 (:)의 앞이나 뒤에 숫자를 입력하지 않으면 맨 앞 또는 맨 뒤를 의미합니다.
# 음의 인덱스를 사용해서 슬라이싱을 할 수 있고, 스텝을 지정할 수도 있습니다.
# 예를 들어, nums[::2]는 튜플 nums를 처음부터 끝까지 2의 스텝으로 슬라이싱합니다.
 


# 튜플 값 변경하기
nums = (1, 2, 3, 4, 5)

nums[1] = 0
# TypeError: 'tuple' object does not support item assignment
# 하지만 리스트와 달리, 튜플은 값을 변경할 수 없습니다. immutable한 datatype이다.


# 튜플 값 삭제하기
nums_list = [1, 2, 3, 4, 5]
del nums_list[0]
print(nums_list)
[2, 3, 4, 5]

nums_tuple = (1, 2, 3, 4, 5)
del nums_tuple[0]
print(nums_tuple)

# TypeError: 'tuple' object doesn't support item deletion
# 또한 del 키워드를 사용해서 리스트의 값을 삭제했던 것과 달리, 튜플의 값은 삭제할 수 없습니다.
# 하지만 튜플 자체를 삭제하는 것은 가능합니다.






# 튜플 메서드 (count(), index())
nums = (1, 1, 3, 2, 5, 3, 2, 1, 4)

print(nums.count(1))
print(nums.index(3))
# 3
# 2
# count(x) 메서드는 튜플에서 값 x가 몇 개 있는지 반환합니다.
# index(x) 메서드는 튜플에서 값 x의 인덱스를 반환합니다. 여러개인 경우 가장 먼저 발견되는 값의 인덱스를 반환합니다.
# 튜플의 기능이 대체로 리스트와 비슷하지만, 리스트와 비교해서 튜플은 아래와 같은 장점을 갖습니다.
# 1.	크기가 큰 경우 리스트에 비해 튜플이 빠른 반복 (iterate) 동작이 가능합니다.

# 2.	튜플이 변경할 수 없는 값들을 갖기 때문에 딕셔너리의 키로 사용할 수 있습니다.


# 즉, 같은 자료형일 때는 리스트를, 다른 자료형의 값들에 대해서는 튜플을 사용하는 것이 좋습니다.

