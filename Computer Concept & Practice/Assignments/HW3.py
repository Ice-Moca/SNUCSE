from functools import reduce

# 1. 지정된 리스트의 홀수 요소 수를 반환하는 함수 f1(list)을 작성하세요.
f1 = lambda li: len(list(filter(lambda n: n % 2 == 1, li)))

# f1([1,2,3,4,5]) 주어진 리스트 li에 대해 filter(lambda n: n%2==1, li)를 통과한 리스트를 다시 만든다.
# 그후 새로운 리스트의 길이를 출력한다. 

# 2. 주어진 리스트에서 각 홀수 요소를 출력하는 함수 f2(list)를 작성하세요.
f2 = lambda li: print(*[elm for elm in list(filter(lambda n: n % 2 == 1, li))], sep="\n")

# f2([1,2,3,4,5]) 주어진 리스트 li에 대해 filter(lambda n: n%2==1, li)를 통과한 리스트를 다시 만든다.
# 그후 새로운 리스트의 원소를 출력한다. 이때 print(*[elm for elm in list],sep='\n')꼴은 *에 의해 반복된다.

# 3. 주어진 리스트에 있는 모든 홀수 요소의 합계를 반환하는 함수 f3(list)을 작성하세요
f3 = lambda li: sum(list(filter(lambda n: n % 2 == 1, li)))

#위의 식에서 sum(list)를 취한 것이다.

# 4. 지정된 리스트에서 요소가 홀수에 해당하는 모든 인덱스의 합계를 반환하는 함수 f4(list)를 작성하세요
f4 = lambda lst: sum([i for i, elem in enumerate(lst) if lst[i] % 2 == 1])

#index와 관련된 값을 반환할때 enumerate() bulit-in function을 쓰자

# 5. 각 요소가 제곱된 동일한 리스트를 반환하는 함수 f5(list)를 작성하세요.
f5 = lambda li: list(map(lambda x: x ** 2, li))

#map()은 iterable한 data의 값들은 loop하듯이 계속 할당해준다.

# 6. 지정된 리스트에서 가장 큰 숫자를 반환하는 함수 f6(list)를 작성하세요. 
f6 = lambda li: reduce(lambda x, y: x if x > y else y, li)

# reduce()는 과정을 반복시켜주는 함수
print(f6([1,2,3,4,5,6,5,4,3,2,1]))

# 7. 주어진 리스트에 있는 모든 숫자의 평균을 반환하는 함수 f7(list)을 작성하세요.
f7 = lambda li: sum(li) / len(li)

# 8. a와 b 포함 범위 내에서 n으로 나누어 떨어질 수 있는 모든 숫자를 출력하는 함수 f8(a,b,n)을 작성하세요. n은 양수라고 가정합니다. 
def f8(a,b,n):
    print(*[row for row in list(filter(lambda x: x % n == 0, range(a,b+1) ))], sep='\n')

# 9. 주어진 너비와 높이로 ASCII 직사각형을 출력하는 함수 f9(width,height)를 작성하세요. 
def f9(width, height):
    any(map( lambda x: print('*'*width), range(0,height) ))

# 10. 주어진 높이 n으로 삼각형을 출력하는 함수 f10(n)을 작성하세요. n이 음수가 아니라고 가정합니다.
def f10(n):
    any(map( lambda x: print('*'*(x+1)), range(0,n) ))

# 11. 리스트가 내림차순으로 정렬되어 있으면 True를 반환하고 그렇지 않으면
# False를 반환하는 함수 f11(list)을 작성하세요. 빈 리스트는 True를 반환합니다. 
def f11(list1):
    return not bool(list(filter( lambda i: list1[i] < list1[i+1], list(range(0,len(list1)-1) ))))

# 12. 리스트가 모든 음수로 구성된 경우 True를 그렇지 않으면 False를 반환하는 함수 f12(list)를 작성하세요. 빈 리스트는 True를 반환합니다. 
def f12(list1):
    return not bool(list(filter( lambda i: list1[i] >= 0, list(range(0,len(list1)) ))))

# 13. 리스트에서 마지막으로 존재하는 target의 인덱스를 반환하는 함수 f13(list, target)을 작성하세요. 리스트가 비어 있지 않고 항상 target이 포함된다고 가정합니다. 
def f13(list1, target):
    return list(filter( lambda i: list1[i] == target, range(0,len(list1)) ))[-1]

# 14. 리스트의 마지막 음수 인덱스를 반환하는 함수 f14(list)를 작성하세요. 리스트가 비어 있지 않고 항상 음수가 포함된다고 가정합니다. 
def f14(list1):
    return list(filter( lambda i: list1[i]<0, range(0,len(list1)) ))[-1]

# 15. 짝수 인덱스의 모든 요소의 합계를 반환하는 함수 f15(list)를 작성합니다. 
def f15(list):
    return sum(list[0::2])

# 16. 거꾸로 된 삼각형을 출력하는 함수 f16(n)을 작성하세요.
def f16(n):
    any(map(lambda x: print('*'*(n-x)), range(n)))

# 17. 리스트의 요소들를 역순으로 2개 건너싹 출력하는 함수 f17(list)을 작성하세요.
def f17(list):
    list.reverse()
    any(map(lambda x: print(list[2*x]) , range(0,(len(list)+1)//2)))

# 18. n!을 반환하는 함수 f18(n)을 작성하세요. 
'''
def f18(n):
  import math; return (math.factorial(n))
'''

def f18(n):
  return 1 if n==0 else n * f18(n-1)
  
# 19. 매트릭스의 각 행의 합계를 출력하는 함수 f19(matrix)를 작성하세요
'''
def f19(matrix):
  s=[sum(row) for row in matrix]
  for i in s:
      print(i)
'''
      
def f19(matrix):
  print(*[sum(row) for row in matrix],sep='\n')

# 20. 매트릭스의 대각선을 출력하는 함수 f20(matrix)을 작성하세요. 행렬이 정사각행렬이라고 가정합니다.
def f20(matrix):
  print(*[matrix[i][i] for i in range(len(matrix))],sep='\n')

# 21. 주어진 목록의 각 요소의 팩토리얼을 출력할 함수 f21(list)을 작성하세요. 
def f21(list):
  import math; print(*[math.factorial(i) for i in list],sep='\n')

# 22. 주어진 리스트에 대해 각 요소에서 0으로 시작하는 카운트다운을 출력하는 함수 f22(list)을 작성하세요
def f22(list1):
  any(map( lambda i: print(*list(range(list1[i], -1, -1))) , range(0, len(list1))))

'''
23. 새 리스트의 각 인덱스가 list1[index] + list2[index]에 해당하는
새 리스트를 반환하는 함수 f23(list1, list2)을 작성하세요. 
list1과 list2의 길이가 같다고 가정합니다. >>> f23([],[])
[]
>>> f23([1,2,3],[1,2,3])
[2,4,6]
>>> f23([0,0,0],[1,2,3,])
[1,2,3]
'''
def f23(list1, list2):
  return [x + y for x, y in zip(list1, list2)]

# 24. 2 또는 3의 배수인 1에서 n까지의 모든 숫자를 출력하는 함수 f24(n)를 작성하세요. 
def f24(n):
  print(*[i for i in range(1, n+1) if i % 2 == 0 or i % 3 == 0], sep='\n')

# 25. 리스트에서 가장 큰 값을 반환하는 함수 f25(list)을 작성하세요(내포된 모든 리스트). 
# 리스트는 중첩된 리스트입니다. 리스트가 비어 있지 않은 것으로 시작한다고 가정합니다. 
def f25(list1):
  return max([ (lambda x: max(x))(x) for x in list1 if len(x)!=0])

# 26. 리스트에서 두 번째로 큰 값을 반환하는 함수 f26(list)를 작성하세요. 리스트의 요소가 모두 고유하고 두 개 이상의 요소가 포함되어 있다고 가정합니다. 
def f26(list):
  print(sorted(list)[-2])

# 27. 가장 왼쪽 자릿수를 반환하는 함수 f27(n)를 n으로 작성하세요. n이 양수라고 가정합니다.
def f27(n):
  return eval(str(n)[0])

# 28. 주어진 리스트에서 각 중첩된 리스트의 가장 큰 값을 인쇄할 함수 f28(list)을 작성허세요. 리스트는 중첩된 리스트입니다. 지정된 리스트의 각 중첩 리스트가 비어 있지 않다고 가정합니다.
def f28(list):
  print(*[max(i) for i in list],sep='\n')