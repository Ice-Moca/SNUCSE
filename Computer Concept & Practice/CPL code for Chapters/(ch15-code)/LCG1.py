# a = 1, c = 7, m = 12
current_x = 0
def prng_seed(s):           # seed generator
      global current_x
      current_x = s

def LCG(n):                 # LCG
    return (n + 7) % 12

def prng( ):
    global current_x
    current_x = LCG(current_x)
    return current_x

prng_seed(6)
[ prng( ) for i in range(12) ]