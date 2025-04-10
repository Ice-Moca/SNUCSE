class A(object): pass
class B(A): pass

a = A()
b = B()

print(type(a) == A) # True
print(type(b) == A) # False
print(type(a) == B) # False
print(type(b) == B) # True
print()
print(isinstance(a, A)) # True
print(isinstance(b, A)) # True (surprised?)
print(isinstance(a, B)) # False
print(isinstance(b, B)) # True