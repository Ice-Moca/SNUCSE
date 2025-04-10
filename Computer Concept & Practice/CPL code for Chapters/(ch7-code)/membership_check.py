import time
n = 50000
a = list(range(2, n+1, 2))
print("Using a list... ", end="")

start1 = time.time( )
count = 0
for x in range(n+1):
    count+=x in a
end1 = time.time ( )
elapsed1 = end1 - start1
print(" time = %0.10f seconds" % elapsed1)

s = set(a)
print("Using a set... ", end="")

start2 = time.time( )
count = 0
for x in range(n+1):
    count+=x in s
end2 = time.time( )
elapsed2 = end2 - start2
print("time = %0.10f seconds" % elapsed2)
print("-----------------------------")
print(" The data size is ", n)
print("sets ran about %0.1f times faster than lists!" % (elapsed1/elapsed2) )
