import time

L = []
S = set()

for n in range(2, 30001, 2):
    L.append(n)
    S.add(n)
print("The size of data = 30000")
 ############# List ################

start = time.time()
count = 0
for x in range(30001):
   if x in L:
      count = count + 1
end = time.time()
time_for_List = end- start
print("Processing time for List = %0.6f seconds" % time_for_List )

############# Set ################

start = time.time()
count = 0
for x in range(30001):
   if x in S:
      count = count + 1
end = time.time()
time_for_Set = end- start
print("Processing time for Set = %0.6f seconds" % time_for_Set )
print()
print("Sets ran about %0.1f times faster than Lists!" % (time_for_List/time_for_Set) )