"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
###
import math

def simple_work_calc(n, a, b):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
	# TODO
	if n == 1:
		return 1

	# The total work is the product of the number of total levels and the work of eahc level. 
	# The number of levels are log_b(n) and the work of an arbitrary level i is n(a/b)^i,
	# Then, we have three cases, each corresponding to geometric series with different ratio r (i.e. |r|=1, |r|>1, |r|<1).

	if a == b:
		totalWork = n*math.log(n,b)
	elif a > b:
		totalWork = n*(((a/b)**(math.log(n,b))-1)/((a/b)-1)) 
	else:
		totalWork = n*((1-((a/b)**(math.log(n,b))))/(1-(a/b)))
	
	return totalWork
	
	pass

def test_simple_work():
	""" done. """
	assert round(simple_work_calc(10, 2, 2)) == 33 #TODO
	assert round(simple_work_calc(20, 3, 2)) == 191 #TODO
	assert round(simple_work_calc(30, 4, 2)) == 870 #TODO
	assert round(simple_work_calc(8, 3, 2)) == 38 #Add 1
	assert round(simple_work_calc(4, 2, 2)) == 8 #Add 2
	assert round(simple_work_calc(1, 4, 2)) == 1 #Add 3
	assert round(simple_work_calc(9, 2, 3)) == 15 #Add 4

def work_calc(n, a, b, f):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
	pass

def span_calc(n, a, b, f):
	"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
	pass

def test_work():
	""" done. """
	assert work_calc(10, 2, 2,lambda n: 1) == #TODO
	assert work_calc(20, 1, 2, lambda n: n*n) == #TODO
	assert work_calc(30, 3, 2, lambda n: n) == #TODO

def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in input_sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			work_fn1(n),
			work_fn2(n)
			))
	return result

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
    
	# create work_fn1
	# create work_fn2

    res = compare_work(work_fn1, work_fn2)
	print(res)

def test_compare_span():
	# TODO
