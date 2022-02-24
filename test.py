from cmath import e
import tabulate
import time
import math 

def simple_work_calc(n, a, b):
	# TODO
	if n == 1:
		return 1
	elif n == 0:
		return 0
	else: 
		return a*simple_work_calc(n//b, a, b) + n

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

print(work_calc(10, 2, 2, lambda n: 1))
print(work_calc(20, 1, 2, lambda n: n*n))
print(work_calc(30, 3, 2, lambda n: n))

print(span_calc(40, 2, 2, lambda n: 1))
print(span_calc(40, 2, 2, lambda n: math.log(n,e)))
print(span_calc(40, 2, 2, lambda n: n))