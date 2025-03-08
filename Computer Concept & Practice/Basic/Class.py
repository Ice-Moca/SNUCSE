
class Ph():
    def __init__(self):
        self.y=5
        self.z=5

    def printHam(self):
        print('ham')

'''
x=Ph()
x.printHam()    #ham이라고 출력
print(x.y)      #x=self가 되고 x.y는 self.y와 같다 즉 __init__는 상수로 작동한다.
print(x,z)      #'Ph'object has no attribute to 'z'
'''
'''
class Ph():
    def printHam():
        print('ham')

#이렇게 하면 self 없어서 작동 안함, self무조건 있어야함
'''
'''
class Class_name(superclasses):
    class_var1
    class_var2                      #클래스 변수:class variable

    def __init__(self,par1,par2):
        self.ins_var1=par1
        self.ins_var2=par2          #인스탄스 변수:instance variable

    def ins_func(self,par1,par2):
        <statement1>
        <statement2>

    @classmethod
    def class_func(cls):
        <statement1>                #클래스 함수:class function=class method
        <statement2>
'''
class Service:
    def sum(self,a,b):
        result=a+b
        print('%s + %s = %s입니다.'%(a,b,result))

pey=Service()
pey.sum(1,1)

class Service_2:
    def __init__(self,name):
        self.name=name

    def sum(self,a,b):
        result=a+b
        print('%s님 %s + %s = %s입니다.'%(self.name,a,b,result))

pey=Service_2('Alex')
pey.sum(2,4)

#pey.name 이건 되는데 Service.name은 안된다.

class BaseClass(object):
    def printHam(self):
        print('ham')
#(object)없어도 똑같이 작동한다.

class ChildClass(BaseClass):
    pass
#BaseClass로부터 함수를 상속받는다. 

'''
x=ChildClass()
x.printHam()

class Foo(object):
    def __init__(self):
        self.health=100
    
class SubFoo(Foo):
    pass

t=SubFoo()
t.health
'''

'''
class Foo(object):
    def __init__(self):
        self.health=100
    
class SubFoo(Foo):
    def __init__(self):
        self.muscle=200

t=SubFoo()
t.health        #Error 뜬다. 만일 Subclass에 상수가 정의되어 있을때 상수가 상속되지는 않는다.
'''

'''
class Foo(object):
    def __init__(self):
        self.health=100
    
class SubFoo(Foo):
    def __init__(self):
        super().__init__()  #여기서는 super()가 Foo로 작동한다. 일반적으로 적절한 superclass로 매치된다.
        self.muscle=200

t=SubFoo()
t.health        #Error 안 뜬다. 상속도 받고 자체적인 변수도 선언한다.
'''

class BaseClass_3(object):
    def test(self):
        print('ham')

class InClass(BaseClass_3):
    def test(self):
        print('hammer time')

I=InClass()
I.test()
#이렇게 함수가 겹칠때는 함수 상속 안됨.

print(BaseClass_3.__subclasses__())             # subclass들을 반환하는 함수. 리스트로 반환
print(InClass.__subclasses__())                 # 없으면 빈 리스트 반환
#InClass.__superclasses__() 이런거는 없음
 
class A:
    def f(self):
        return self.g()
    def g(self):
        return 'A'
    
class B(A):
    def g(self):
        return 'B'
    
a=A()
b=B()

print(a.f(),b.f())          #이때 f()는 상속되지만 g()는 상속되지 않는다 
print(a.g(),b.g())          #이때 f()에서 반환되는 g()가 A클라스인지 B클라스인지에 따라 변한다.


class Person:
    def speak(self):
        print('I can speak')

class Man(Person):
    def wear(self):
        print('I wear shirt')

class Woman(Person):
    def wear(self):
        print('I wear skirt')

man=Man()
man.wear()          # I wear shirt
print(man.wear())   # I wear shirt \n None 1.man.wear()이 실행되고 2. print(print())꼴이라 None값


# Constructor __init__()
# Destructor __del__(): del A 꼴로 작성하면 코드 실행 후 삭제

class Person:
    def __init__(self,name):
        self.name=name
        print(self.name)
    def Sayhello(self):
        print('Hello my name is %s' %self.name)
    def __del__(self):
        print('delete')

A=Person('HamHam')
A.Sayhello()
del A

'''
import sys
sys.getrefcount(obj) : object obj에 대한 참조 갯수를 반환하는 함수

sys.getrefcount(3): 3을 가르키는 포인터의 개수 (객체지향) 
a=3, b=3 처럼 포인터 추가 --> sys.getrefcount값도 증가 
'''

#Super Class생성 : 여러가지 class를 대표하는 class를 만들고 싶을때
'''
class Foo(object):
    def __init__(self):
        self.health=100
    
class SubFoo(Foo):
    def __init__(self):
        super().__init__()  #여기서는 super()가 Foo로 작동한다. 일반적으로 적절한 superclass로 매치된다.
        self.muscle=200
'''

# issubclass(sub,sup): return true if subclass is indeed a subclass of the sup
# isinstance(obj,Class): return true if obj is instance of class Class or instance of subclasses of Class

class A:
    def A(self):
        print('I am A')

class B:
    def A(self):
        print('I am a')
        
    def B(self):
        print('I am B')

class C(A,B):
    def C(self):
        print('I am C')

# left to right sequence에 의해 c.A()는 A.A()를 실행
# C(B,A)로 대입하면 c.A()는 B.A()가 나온다
c=C()
c.A()
c.B()

'''
<Java>
Private variable and methods : 선언된 class 내부에서만 접근 가능
Protected variable and methods : 선언된 class와 subclass에서만 접근 허락 
Public variable and methods : 어디서든지 접근 허락
'''
# python there is no keywords like 'public', 'protected', 'private'

# To define Private in Python: add __ in front of the variable and 
# function name can hide them when accessing them from out of class

# 외부에서 직접 access는 불가능하고 함수를 실행할 때만 외부에서 볼 수 있다

class Person:
    def __init__(self):
        self.A = 'Yang Li'          # Public Variable
        self.__B = 'Yangying gu'    # Private Variable
    
    def PrintName(self):
        print(self.A)
        print(self.__B)             # Invoke(호출) private variable in class

P=Person()
P.PrintName()

class Justcounter:
    __secretCount =0 
    def count(self):
        self.__secretCount +=1
        print(self.__secretCount)
'''   
counter = Justcounter()
counter.count()
counter.count()

print(counter._Justcounter__secretCount)           # object._className__attrName으로는 접근 가능하다. (교제 오류)

print(counter.__secretCount)                        # counter object를 통해서라도 class밖에서  __secretCount는 access금지
''' 
class hello:
    var1=10
    __var2=20
    def print_var1(self):
        print(self.var1)

    def __print_var1(self):
        print(self.var1)
        
    def print_var2(self):
        print(self.__var2)
        
    def __print_var2(self):
        print(self.__var2)
'''
a=hello()
print(a.var1)           # 10
print(a.__var2)         # Error
a.print_var1()          # 10
a.__print_var1()        # Error
a.print_var2()          # 20 클래스 내부에서 구동되기 때문에 가능하다.
a.__print_var2()        # Error
'''

# Instance Variable vs Class Variable

# Instance Variable: 각각의 Instance마다 다른 값을 가지는 variable :변수 느낌
# Class Variable: Class의 모든 Instance에 공통적인 값을 가지는 variable : 상수 느낌

# Instance Method : 각각의 Instance에 적용되는 함수들 gpa(name)같은 느낌
# Class Method: Class 내부 전체 instance에 적용되는 method avg_gpa()같은 느낌


class Person:
    'Common base class for people'  # Documentation으로 클래스에 대한 설명 제시
    lastname='Park'                  # class variable
    def __init__(self):         
        self.A = 'Yang Li'          # Instance variable 중 Public Variable    
        self.__B = 'Yangying gu'    # Instance variable 중 Private Variable
    
    def PrintName(self):
        '이름을 써라'                # Documentation으로 함수에 대한 설명 제시
        print(self.A)
        print(self.__B)             # Invoke(호출) private variable in class

    @classmethod
    def class_foo(cls):
        print('excluding class_foo')


print(Person.__doc__)               
print(Person.PrintName.__doc__)     #이거는 Person.PrintName이 call이 안되도 결과값이 출력된다

'''
Class.__name__          # 클래스의 이름 반환
Class.__module__        # 클래스가 정의된 모듈의 이름 반환
Class.__bases__         # Superclasses를 보여준다
Class.__dict__          # 클래스 내부의 모든 symbol들에 대해서 Dictionary 형태 (symbol:value)로 반환
'''

JJ=Person()
print(Person.lastname)              # class Method
print(JJ.A)                         # instnace Method              

Person.class_foo()                  # 클래스매써드를 지정할 수 있다.
JJ.class_foo()                      # instance JJ에서 call할 수 있다.
'''
Person.PrintName()                  # class.Instance_Method는 call할 수 없다.
'''
class MC:
    def __init__(self):
        self.size=10
        self.data=list(range(self.size))
    
    def __iter__(self):
        self.index=0
        return self
    
    def __next__(self):
        if self.index>=self.size:
            raise StopIteration
        n=self.data[self.index]
        self.index+=1
        return n
    
C=MC()
for x in C:
    print(x)

def gen():
    yield 1
    yield 2
    yield 3

g=gen()
print(type(g)) #<class 'generator'>

print(next(g))
print(next(g))
print(next(g))

for x in gen():
    print(x)

