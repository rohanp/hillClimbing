from math import sin, cos

def ftup(*args):
	s = ''
	for arg in args:
		sub = '('
		for a in arg:
			sub += str( round(a, 2) ) + ', '
		s += sub[:-2] + ') = %s \n'%f(*arg)
	return s

def f(*xy):
	return xy[0] * sin(4*xy[0]) + 1.1*xy[0]*sin(2*xy[0]) if 0 < xy[0] < 10 and 0 < xy[1] < 10 else float('inf')
