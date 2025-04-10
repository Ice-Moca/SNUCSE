def pi_series_iter(n):
	result = 0
	for i in range(1, n+1):
		result = result + 1/(i**2)
	return result

def pi_iter(n):
	x=pi_series_iter(n)
	return (6*x)**(.5)

def pi_series_r(i):
	assert(i>=0)
	if i==0:
		return 0
	else:
		return pi_series_r(i-1) + 1/ i**2

def pi_r(n):
	x=pi_series_r(n)
	return (6*x) **(.5)

def test_pi():
	for i in range(996):
		assert pi_iter(i)==pi_r(i)
		if (i%100==0):
			print("Value of i: ", i)
			print("Iterative PI: ", pi_iter(i), "  vs  Recursion PI: ", pi_r(i))
	print("Done testing pi approximations")

test_pi()