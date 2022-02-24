"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
from cmath import e
import tabulate
import time
###
import math

def simple_work_calc(n, a, b):
	# TODO
	if n == 1:
		return 1
	elif n == 0:
		return 0
	else: 
		return a*simple_work_calc(n//b, a, b) + n

def test_simple_work():
	assert simple_work_calc(10, 2, 2) == 36 #TODO
	assert simple_work_calc(20, 3, 2) == 230 #TODO
	assert simple_work_calc(30, 4, 2) == 650 #TODO
	# Additional three cases:
	assert simple_work_calc(1, 2, 2) == 1
	assert simple_work_calc(40, 2, 3) == 90
	assert simple_work_calc(50, 4, 3) == 258


def work_calc(n, a, b, f):
	# TODO
	if n == 1:
		return 1
	elif n == 0:
		return 0
	else:
		return a*work_calc(n//b, a, b, f) + f(n)

def span_calc(n, a, b, f):
	# TODO
	if n== 1:
		return 1
	elif n == 0:
		return 0
	else:
		return span_calc((n//b), a, b, f) + f(n)
	

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15 #TODO
	assert work_calc(20, 1, 2, lambda n: n*n) == 530 #TODO
	assert work_calc(30, 3, 2, lambda n: n) == 300 #TODO
	# Additional three cases:
	assert work_calc(40, 4, 2, lambda n: n+1) == 2477
	assert work_calc(50, 2, 4, lambda n: n) == 86
	assert work_calc(60, 3, 3, lambda n: n*n) == 5232

def compare_work(work_fn1, work_fn2, work_fn3, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			work_fn1(n),
			work_fn2(n),
			work_fn3(n)
			))
	return result

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2', 'W_3'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
    
	# create work_fn1
	# create work_fn2
	work_fn1 = lambda n:work_calc(n, 8, 2, lambda n: n**4) # let c be 4 which > log_b(a)
	work_fn2 = lambda n:work_calc(n, 8, 2, lambda n: n**2) # let c be 2 which < log_b(a)
	work_fn3 = lambda n:work_calc(n, 8, 2, lambda n: n**3) # let c be 3 which = log_b(a)
	res = print_results(compare_work(work_fn1, work_fn2, work_fn3))
	print(res)

def test_compare_span():
	work_fn1 = lambda n:span_calc(n, 8, 2, lambda n: 1) # f(n) = 1
	work_fn2 = lambda n:span_calc(n, 8, 2, lambda n: math.log(n,e)) # f(n) = logn
	work_fn3 = lambda n:span_calc(n, 8, 2, lambda n: n) # f(n) = n
	res = print_results(compare_work(work_fn1, work_fn2, work_fn3))
	print(res)
	# TODO

test_compare_span()