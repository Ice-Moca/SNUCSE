def fac_iter(n):
	factor = 1
	for i in range(2, n+1):
		factor = factor * i
	return factor

def fac_rec(n):
	if (n<2):
		return 1
	else:
		return n*fac_rec(n-1)

def factorial(n, depth=0):
	print(" " * depth, " factorial(" , n, ") ", n, "! = ", n, "*", (n-1), "!")
	if (n<2):
		return 1
	else:
		return n*factorial(n-1, depth +1)


print(fac_iter(5))
print(fac_rec(5))
factorial(5)