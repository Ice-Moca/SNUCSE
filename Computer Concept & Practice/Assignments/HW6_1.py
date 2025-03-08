# Advanced OOP (1번): Point Class & Pythagoras Class

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Pythagoras:
    def setPointOne(self, point):
        self.point_one = point
    
    def setPointTwo(self, point):
        self.point_two = point

    def getSlope(self):
        return (self.point_two.y - self.point_one.y) / (self.point_two.x - self.point_one.x)
    def getDistance(self):
        return ((self.point_two.y - self.point_one.y)**2 + (self.point_two.x - self.point_one.x)**2)**0.5
    
    # Advanced OOP (2번) : Calculator Class

class Calculator:
    
    history = []
    expression = ''
    result = 0

    def add(self, num):
        if self.expression == '':
            self.expression += str(num)
        else:
            self.expression += ' + ' + str(num)

        self.result += num
    
    def subtract(self, num):
        self.expression += ' - ' + str(num)

        self.result -= num

    def multiply(self, num):
        self.expression += ' * ' + str(num)

        self.result *= num

    def equals(self, print_msg=False):
        if self.expression == '':
            print("No calcutaion done yet!")
        else:
            self.expression += ' = ' + str(self.result)
            if print_msg == True:
                print(self.result)
            self.history.append(self.expression)
            self.expression = ''
            self.result = 0
        
    
    def showHistory(self):
        print('History:')
        for expression in self.history:
            print(expression)
        
# test = Calculator()
# test.equals()
# test.showHistory()

# test.add(2)
# test.subtract(1)
# test.equals()
# test.showHistory()

# test.add(2)
# test.multiply(4)
# test.equals(True)

# test.add(10)
# test.subtract(5)
# test.multiply(2)
# test.equals()

# test.showHistory()


# Advanced OOP (3번): Account Class [1/2]

class Account:

    transactions = []

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    
    def deposit(self, amount):
        """
        Increase the account balance by amount and return the new balance.
        """
        self.balance = self.balance + amount

        self.transactions.append( ('deposit', amount) )
        # return self.balance

    def withdrawal(self, amount):
        """
        Decrease the account balance by amount and return the new balance.
        """
        if amount > self.balance:
            return "Insufficient funds"
        self.balance = self.balance - amount

        self.transactions.append( ('withdrawal', amount) )
        # return self.balance

    def status(self):
        print(self.holder+": ", end="")
        print(self.transactions)

# bob_account = Account("Bob")
# bob_account.deposit(100)
# bob_account.withdrawal(1000)
# bob_account.deposit(400)
# bob_account.status()

# Advanced OOP (4번): Atom and Molecule [1/2]

Atno_to_Symbol = {1:'H',2:'He',3:'Li',4:'Be',5:'B',6:'C',7:'N',8:'O'}
class atom(object):
    def __init__(self,atno,x,y,z):
        self.atno = atno
        self.position = (x,y,z)
    def symbol(self):
        return Atno_to_Symbol[self.atno]
    def __repr__(self):
        return '%d %10.4f %10.4f %10.4f' % (self.atno,self.position[0],self.position[1],self.position[2])
## atom class explanation ##
    # self.atno -> 원자의 원자번호를 담는 variable
    # self.position -> 원자의 위치(x,y,z)를 저장하는 variable
    # self.symbol() -> 원자의 원소기호를 반환하는 method

class molecule:
    def __init__(self, name='Generic'):
        self.name = name
        self.atomlist = []
    def addatom(self,atom):
        self.atomlist.append(atom)
    def __repr__(self):
        str = 'This is a molecule name %s\n' % self.name
        str = str + 'It has %d atoms\n' % len(self.atomlist)
        for atom in self.atomlist:
            str = str + "%s\n" % atom
        return str
## molecule class explanation ##
    # self.name -> 분자의 이름은 저장하는 variable (기본값은 Generic)
    # self.atomlist -> 분자 안의 원자들을 저장하는 리스트 형식의 variable
    # self.addatom() -> self.atomlist에 원자를 추가하는 method

    # Advanced OOP (4번): Atom and Molecule [2/2]

at = atom(6, 0.0, 1.0, 2.0)
print(at)
# output: 6     0.0000     1.0000     2.0000
print(at.symbol())
# output: C

mol = molecule('Water')
at = atom(8,0.,0.,0.)
mol.addatom(at)
mol.addatom(atom(1,0.,0.,1.))
mol.addatom(atom(1,0.,1.,0.))
print(mol)
# output:
# This is a molecule name Water
# It has 3 atoms
# 8     0.0000     0.0000     0.0000
# 1     0.0000     0.0000     1.0000
# 1     0.0000     1.0000     0.0000


# Advanced OOP (5번): Professor and Student

class Person:
    def __init__(self, name, depart):
        self.name = name
        self.depart = depart
    def getName(self):
        return self.name
    def getDepart(self):
        return self.depart
    
class Student(Person):
    def __init__(self, name, depart,year,credit):
        super().__init__(name, depart)
        self.year = year
        self.credit = credit
    def getCredit(self):
        return self.credit
    def setCredit(self, credit):
        self.credit = credit
    def increaseYear(self):
        self.year = self.year + 1

class Professor(Person):
    def __init__(self, name, course, depart, salary):
        super().__init__(name, depart)
        self.course = course
        self.salary = salary

    def getCourse(self):
        return self.course
    def getAnnualSalary(self):
        return 12 * self.salary
    def raiseSalary(self, percent):
        self.salary *= (1+percent/100)

# Advanced OOP (5번): Professor and Student Using the class created in the previous page:

tim_cook = Professor('Tim Cook', 'Soft. Arch.','CSE',5500)

print( 5 * tim_cook.getAnnualSalary())
count = 0
for i in range(5):
    count += tim_cook.getAnnualSalary()
    tim_cook.raiseSalary(15)
print(count)



#Advanced OOP (6번): Staff and Student [1/3]

class Person:
    def __init__(self,name,address):
        self.name = name
        self.address = address
    def getName(self):
        return self.name
    def getAddress(self):
        return self.address

class Staff(Person):
    def __init__(self,name,address,school,annual_pay):
        self.name = name
        self.address = address
        self.school = school
        self.annual_pay = annual_pay
    def getSchool(self):
        return self.school
    def getMonthlyPay(self):
        return self.annual_pay/12
    def raiseAnnualPay(self, percent):
        self.annual_pay = (1+percent/100)*self.annual_pay

class Student(Person):
    def __init__(self,name,address,year):
        self.name = name
        self.address = address
        self.year = year
    def getGpa(self):
        return self.GPA
    def setGpa(self, GPA):
        self.GPA = GPA
    def hasMinimunGpa(self):
        if self.GPA >= 3.5:
            return True
        else:
            return False
    def willGraduateNextYear(self):
        if self.year == 4:
            return True

tom=Staff('Tom','Gangnam','Yonsei',35000)
dane=Staff('Dane','Shindorim','Sogang',20000)
for i in range(7):
    tom.raiseAnnualPay(7)
    dane.raiseAnnualPay(15)
if tom.annual_pay > dane.annual_pay:
    print('Tom has a larger monthly pay')
elif tom.annual_pay == dane.annual_pay:
    print('same')
else:
    print('Dane has a larger monthly pay')
