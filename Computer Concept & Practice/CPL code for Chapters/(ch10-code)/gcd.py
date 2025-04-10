def gcd_iter(x,y):
    while(y > 0):
        oldx = x
        x = y
        y = oldx % y
    return x


def gcd_rec(x,y):
    if (y == 0):
        return x
    else:
        return gcd_rec(y, x%y)


def gcd(x,y,depth = 0):
    if (y == 0):
        return x
    else:
        print(" " *depth, "gcd(" , x, ", " , y, "): x%y (remainder) = ", x%y)
        return gcd(y, x%y, depth + 1)



gcd(500, 420)