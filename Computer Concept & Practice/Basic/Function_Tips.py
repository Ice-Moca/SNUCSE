# regular parameter vs optional parameter
# 간단히 말하자면 optional parameter의 경우 입력값이 없어도 작동 가능하다.

def f(x,y=10):
    return x+y

print(f(10))       #20
print(f(10,3))     #13

# f(*args) 이런 꼴은 여러개의 입력값이 들어오는 것을 기대하는 parameter이다.
print(*[1,2,3,4,5],sep='\n') #이런식으로 작성 iterable한 데이터와 혼용해서 주로 이용

#리스트와 튜블, 집합을 잘 구분하자.

# TIme 라이브러리
# time.time(): 1970년 1월 1일 부터 현재까지의 시간을 표시
# 함수의 작동시간 측정할때 나중값-초기값으로 하자

# set() != {} {}는 dictionary 표현이다.

# Aliasing (논리적 복제) vs Copy (물리적 복제)
# import copy
# copy.copy()  사용하면  물리적인 복제이다. 즉 포인터가 아님

# b=a

# b=a[:]
# b=copy(a)
# b=a+[]
# b=list(a)

# b=copy.deepcopy(a)

'''
all() any() chr() ord() eval()
# all([1,2,3]) : [1,2,3]의 모든 요소가 True 이므로 True 반환 
# any([1,2,3]) : [1,2,3]의 요소 중 하나라도 True 이므로 True 반환 
# chr(97) : 아스키 --> 문자 반환
# ord(a) : 문자 --> 아스키 (integer) 반환
# eval('a'): 문자--> 따옴표 제거한 것으로 반환
'''

'''
file_obj=open(filename, 'mode') 로 입력
mode : w 쓰기, r 읽기, a 추가하기, b 바이너리 모드로 열기
w: File 내용을 새로운 내용으로 교체, 없으면 새로 생성한다.
r: 읽기 모드로 파일을 연다. File이 존재하는 걸 가정하기에 File 없으면 Error발생
a: 파일 맨뒤에 새로운 내용을 추가. File이 존재하는 걸 가정하기에 File 없으면 Error발생
b: binary모드로 열기
t: Text mode로 파일 열기(Default)
w+: w+r
r+: r+w : r에 w를 추가하지만 기존의 파일 내용을 제거하지 않는다. 
파일이 없어도 생성하지 않는다. 파일 있다고 가정한다 즉 없으면 에러 발생

(w,r,a,r+,w+)+(t,b)=(x,y)꼴로 파일 오픈 모드 설정한다.

import os
os.chdir("C:\\Users\\something\\Desktop")
os.chdir(r"C:\Users\something\Desktop")
os.chdir("C:/Users/something/Desktop")

#위의 세식 모두 바탕화면의 파일을 Python working director로 설정


myfile=open('filename', 'w')
for i in range(10):
    data='This is line %d. \n' %i
    myfile. write(data)
myfile.close()

#close해야 write한 데이터 내용이 파일에 반영된다.
다시 쓰면 파일의 내용을 새로운 내용으로 교체하는 것것

filename.txt
This is line 1.
.
.
.

myfile=open(filename, 'a')
for i in range(10):
    data='This is line %d. \n' %(i+10)
    myfile. write(data)
myfile.close()
'a'이기 때문에 파일뒤에 새로운 내용 추가

myfile=open(filename, 'r')
line = myfile. readline()
print(line)
myfile.close()

myfile=open(filename, 'r')
for i in range(10):
    line=myfile. readline()
    print(line)
myfile.close()
    
한줄씩 전진하며 읽는 것을 반복하는 함수이다.
File pointer: beginning of file에서 전진

myfile=open(filename, 'r')
lines=myfile. readlines()
for line in lines
    print(line)
myfile.close()

# 파일의 모든 라인을 string으로 받아 list로 만든다.

myfile=open(filename, 'r')
data=myfile. read()
print(data)
myfile.close()

#파일의 모든 내용을 1개의 string으로 반환한다.
#'This line 1.\nThis line 2.\n...' 이런식으로 반환

#close() with문을 사용하면 close()안써도 자동으로 close된다.
with open('filename','w') as f:
    f.write('something')

with open('Filename ') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

with open('Filename ') as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

with open('Filename ') as file_object:
    lines = file_object.readlines()
p=''
for line in lines:
    p=p+line.rstrip()
print(p)
# 쭉 이어진 string이 나옴

#rstrip() : 마지막 줄에 있는 \n을 제거하기 위함 (원래 저함수는 string에서 우측 끝의 빈칸과 \n을 제거한다)
#str='H \n\n' str.strip() --> 'H'
#str='A8888888' A.rstrip('8') ---> 'A'

with open('Filename ') as file_object:
for line in file_object:
    print(line)

myfile.seek(0.0)은 파일 포인터의 위치 초기화
myfile.close()를하고 다시 open()으로 열어도 위치 초기화된다.
'''

# assert 키워드: 뒤의 값 True면 진행 아니면 Error발생
# zip(): 동일 index의 리스트를 묶어 Tuple로 이루어진 List로 반환해준다.

'''
try: 뭐시기
execpt 뭐시기 에러: 뭐시기
    pass #그냥 아무것도 안하는 키워드
finally:
    뭐시기 #finally는 exception 발생 여부와 관계없이 꼭 수행하는 코드이다.

이렇게 쓰면 명시된 에러를 처리한다.
그리고 다음줄로 넘어감. 명시된 에러 없을때는 다음줄로 그냥 진행한다.

ZeroDivisionError
ValueError
NameError
TypeError
IndexError
FileNotFoundError
'''

'''
from demical import *
getcontext().prec=6
#소수 6번째자리까지 정확한 값을 얻는다

Decimal(1)/Decimal(7)
>>>Decimal('0.142857')
'''