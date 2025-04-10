
class HousePark:
    lastname = "박"
    
    def __init__(self, name):
        self.fullname = self.lastname + name
        
    def travel(self, where):
        print("%s, %s여행을 가다." % (self.fullname, where))
        
    def love(self, other):
        print("%s, %s 사랑에 빠졌네" % (self.fullname, other.fullname))
        
    def __add__(self, other):
        print("%s, %s 결혼했네" % (self.fullname, other.fullname))
    #__add__()는 + 로도 작동, 즉 class내부에 __add__()정의되야함. [2,4]+[5]-->[2,4,5] 와 같은 원리
    #__sub__()는 - 로도 작동
    
class HouseKim(HousePark):
    lastname = "김"
    
    def travel(Self, where, day):
        print("%s, %s여행 %d일 가네." % (self.fullname, where, day))
        
pey = HousePark("응용")
juliet = HouseKim("줄리엣")
pey.love(juliet)
pey + juliet

print(issubclass(HouseKim,HousePark))

# IS-A semantics 
# Rectangle Class 있을떄
'''
class Window(Rectangle):
    inherit Rectangle
    add operation 
    def __add__(self,other):
        뭐시기
'''
# 과정이 추가되면서 함수가 점점 추가 되면 More specific하다고 한다.
# 하지만 상속된 값 중에 변한게 있으면 IS-A Semantics(의미론적) 관계는 아니라고 본다.
