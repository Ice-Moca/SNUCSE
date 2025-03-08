def f1(lst):
  if len(lst) == 1:
    return lst[0]
  elif len(lst)==0:
    return 0
  else:
    return lst[0]+f1(lst[1:])

def f(n):
  if n%2==0:
    return n//2
  else: return 3*n+1

def f2(n):
  if n==1:
    return 1
  else:
    return 1+f2(f(n))

def f3(lst):
  if len(lst)==1:
    print(lst[0])
  elif len(lst)==0:
    return None
  else: 
    print(lst[len(lst)-1]) 
    return f3(lst[0:len(lst)-1])

def f4(lst):
  if len(lst)==1:
    if lst[0]%2==1: 
     print(3*lst[0])
  elif len(lst)==0:
     return None
  else: 
    if lst[0]%2==1:
     print(3*lst[0])
    return f4(lst[1:])

def f5(lst):
    if lst == []:
        return
    else:
        if lst[-1] % 2:
            print(lst[-1] * 3)
        else:
            print(lst[-1])
        f5(lst[:-1])
      
def f6(lst):
    if len(lst) == 0:
        return lst
    if type(lst[0])== list:
        return f6(lst[0]) + f6(lst[1:])
    return lst[:1] + f6(lst[1:])
  

def f7(n):
  if n==1:
    return 1
  elif n==0:
    return 2
  else:
    return f7(n-1)+f7(n-2)

def f8(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    else:
        return f8(s[1:-1])

def f9(n):
  if n==0:
    return 1
  else:
    return n*f9(n-1)

def f10(lst):
  if lst==[lst[0]]:
    return 1
  else: 
    return 1+f10(lst[1:])

def f11(lst):
  if len(lst)==1:
    return lst[0]
  elif len(lst)==0:
    return None
  else: return f11(lst[1:])

def f12(n):
  if n==1:
    print(1)
  elif n==0:
    return None
  else: 
    print(n) 
    return f12(n-1)

def f13(n):
  if n>=10:
    return 1+f13(n//10)
  else:
    return 1
    
def f14(lst):
  if len(lst)==1:
    if lst[0]%2==1:
      return lst[0]
    else: return None
  elif len(lst)==0:
    return None
  else:
    if lst[0]%2==1:
      return lst[0]
    else: return f14(lst[1:])

def f15(lst):
    if len(lst) == 0:
        return 0
    elif lst[0] % 2==1:
        return lst[0] + f15(lst[1:])
    else:
        return f15(lst[1:])

def f16(lst):
    if len(lst)==0:
        return lst
    else:
        if lst[0]%2 == 1 :
            return [lst[0]]+f16(lst[1:])
        else:
            return f16(lst[1:])

def f17(lst):
    if len(lst)==2:
        return lst[0]
    else:
        return f17(lst[1:])

def f18(a,b):
    if a%b ==0:
        return b
    else:
        return f18(b,a%b)

def f19(lst1, lst2):
    i, j = 0, 0
    new_lst = []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            new_lst.append(lst1[i])
            i += 1
        else:
            new_lst.append(lst2[j])
            j += 1
    new_lst.extend(lst1[i:])
    new_lst.extend(lst2[j:])
    return new_lst

def f20(lst):
    if len(lst) <= 1:
        return lst
    return f19(f20(lst[:len(lst) // 2]), f20(lst[len(lst) // 2:]))

def work_odd_or_even():
    n = input("What number are you thinking? ")
    while n != "No":
        work = "odd" if int(n) % 2 else "even"
        print(f"That's an {work} number!\n")
        n = input("Have another? ")
    print("Have a nice day!")

def BiographyInfo():
  text_list = [
    "이름을 입력하세요: ",
    "태어난 날짜를 입력하세요: ",
    "주소를 입력하세요: ",
    "personal goals를 입력하세요: "
  ]
  values = [0,0,0,0]
  i = 0
  while i < 4:
    _input = input(text_list[i])
    if _input == '':
      continue
    if _input[0] == '*':
      print("다시 제대로 된 정보를 입력하세요")
      continue
    values[i] = _input
    i+=1
  print("Name:", values[0])
  print("Date of birth:", values[1])
  print("Address:", values[2])
  print("Personal goals:", values[3])

def play_rps_game():
  from random import randint
  choice = ['rock','paper','scissors']
  win = { # win[win] == lose
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
  }
  print("가위바위보 놀이요")
  while True:
    _input = input('your choice? ')
    if _input == 'Q':
      print('좋은 날 되십시오')
      break
    
    if _input not in choice:
      print("다시 입력하세요")
      continue
    computer = choice[randint(0,2)]
    print("computer choice:", computer)
    if _input == computer:
      print("draw")
    elif win[_input] == computer:
      print('you win')
    else:
      print("computer win")




def runPalindromeCheck(s):
    s = "".join(c for c in s if c.isalpha()).lower()
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def email_slicer():
  A = input('What is your email address?: ')
  if '@' in A:
    a=A[0:A.index('@')]
    b=A[A.index('@')+1:]
    print('Your username is "%s" and your domain name is "%s"' %(a,b) )
  else:
    return email_slicer()
  
  def greet_user(username):
    """DIsplay a simple greeting."""
    print("Hello, "+ username.title()+'!')

greet_user('jesse') # type: ignore

#Hello, Jesse!

def describe_pet(pet_name,animal_type='dog'):
    """Display information about a pet"""
    print('\nI have a '+animal_type + '.')
    print('My '+ animal_type + "'s name is "+ pet_name.title()+ '.')

# A dog named Willie
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry
describe_pet('harry','hamster')
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet(animal_type='hamster',pet_name='harry')

# I have a dog.
# My dog's name is Willie.

# I have a dog.
# My dog's name is Willie.

# I have a hamster.
# My hamster's name is Harry.

# I have a hamster.
# My hamster's name is Harry.

# I have a hamster.
# My hamster's name is Harry.

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name=first_name+''+middle_name+''+last_name
    else:
        full_name=first_name+''+last_name
    return full_name.title()

musician= get_formatted_name('jimi','hendrix')
print(musician)
musician= get_formatted_name('john','hooker','lee')
print(musician)

# Jimihendrix
# Johnleehooker

def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person={'first' : first_name, 'last' : last_name}
    if age:
        person['age']=age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# {'first': 'jimi', 'last': 'hendrix', 'age': 27}

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = 'Hello, ' + name.title() + '!'
        print(msg)

usernames= ['hannah', 'try', 'margot']

greet_users(usernames)

# Hello, Hannah!
# Hello, Try!
# Hello, Margot!

def print_models(unprinted_designs,completed_models):
    """
    Simulate printing each design, until there are none left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design= unprinted_designs.pop()

        # Simulate creating a 3d print from the design.
        print('Printing model: '+ current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print('\nThe following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

# Printing model: dodecahedron
# Printing model: robot pendant
# Printing model: iphone case

# The following models have been printed:
# dodecahedron
# robot pendant
# iphone case

def make_pizza(size,*toppings):
    """Summarize the pizza we are about to make"""
    print('\nMaking a '+str(size)+ '-inch pizza with the following toppings:')
    for topping in toppings:
        print('-'+topping)

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

# Making a 16-inch pizza with the following toppings:
# -pepperoni

# Making a 12-inch pizza with the following toppings:
# -mushrooms
# -green peppers
# -extra cheese

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile

user_profile = build_profile('albert','Einstein',location='princeton',field='physics')

print(user_profile)

# {'first_name': 'albert', 'last_name': 'Einstein', 'location': 'princeton', 'field': 'physics'}

# pizza.py
def make_pizza(size,*toppings):
    """Summarize the pizza we are about to make"""
    print('\nMaking a '+ str(size)+ '-inch pizza with the following toppings:')
    for topping in toppings:
        print('-'+ topping)


make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers', 'extra cheese')

# Making a 16-inch pizza with the following toppings:
# -pepperoni

# Making a 12-inch pizza with the following toppings:
# -mushrooms
# -green peppers
# -extra cheese

def first_perfect_square(numbers):
    for i in range(len(numbers)):
        if numbers[i] > 0:
            if (numbers[i]**(0.5))==(numbers[i]**(0.5))//1:
                return i
    
    return -1

def num_perfect_square(numbers):
    result = 0
    for i in range(len(numbers)):
        if numbers[i] > 0:
            if (numbers[i]**(0.5))==(numbers[i]**(0.5))//1:
                result+=1 
    return result


def second_largest(values):
    max_index= 0
    for i in range(len(values)):
        if values[i] >= values[max_index]:
            max_index=i
            second_index=i-1
    for j in range(len(values)):
        if j != max_index:
            if values[j]>= values[second_index]:
                second_index=j
    return values[second_index]

'''
print(second_largest([3,-2,10,-1,5]))
print(second_largest([1,2,3,3]))
print(second_largest([-2,1,1,-3,5]))
print(second_largest([3.1,3.1]))
print(second_largest(['apla','beta','gamma','delta']))
print(second_largest([True,False,True,False]))
print(second_largest([True,False,False]))
'''