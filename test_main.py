from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36 #TODO
	assert simple_work_calc(20, 3, 2) == 230 #TODO
	assert simple_work_calc(30, 4, 2) == 650 #TODO
	# Additional three cases:
	assert simple_work_calc(1, 2, 2) == 1
	assert simple_work_calc(40, 2, 3) == 90
	assert simple_work_calc(50, 4, 3) == 258

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15 #TODO
	assert work_calc(20, 1, 2, lambda n: n*n) == 530 #TODO
	assert work_calc(30, 3, 2, lambda n: n) == 300 #TODO
	# Additional three cases:
	assert work_calc(40, 4, 2, lambda n: n+1) == 2477
	assert work_calc(50, 2, 4, lambda n: n) == 86
	assert work_calc(60, 3, 3, lambda n: n*n) == 5232
