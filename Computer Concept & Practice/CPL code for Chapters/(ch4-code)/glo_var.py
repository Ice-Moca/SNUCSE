glVar = 5

def myFunc1():
    global glVar
    var = 100
    glVar = glVar - 10
    print('Current glVar: ', glVar, '  Local variable: ', var)

def myFunc2():
    global glVar
    glVar = glVar + 10
    print('Current glVar: ', glVar)

myFunc1()
myFunc2()  
