from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 10*math.log(10,2) #TODO
	assert simple_work_calc(20, 3, 2) == 40*(((3/2)^(math.log(20,2)))-1) #TODO
	assert simple_work_calc(30, 4, 2) == 870 #TODO
	assert simple_work_calc(8, 3, 2) == 38 #Add 1
	assert simple_work_calc(4, 2, 2) == 8 #Add 2
	assert simple_work_calc(1, 4, 2) == 1 #Add 3
	assert simple_work_calc(9, 2, 3) == 15 #Add 4

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == #TODO
	assert work_calc(20, 1, 2, lambda n: n*n) == #TODO
	assert work_calc(30, 3, 2, lambda n: n) == #TODO
