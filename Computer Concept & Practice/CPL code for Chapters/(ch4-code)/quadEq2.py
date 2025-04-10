import math
def quadEq2():
    print("This program finds the real solutions to a quadratic!")
    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
    print("You want to solve %dX*X + %dX + %d = 0  Right?" %(a,b,c))
    discrim = b * b - 4 * a * c
    if discrim < 0:
        print("\nThe equation has no real roots!")
    elif discrim == 0:
        root = -b / (2 * a)
        print("\n There is a double root at", root)
    else: # discrim > 0
        discRoot = math.sqrt(discrim)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\n The solutions are:", root1, root2 )
