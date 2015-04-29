__author__ = "Rohan Pandit"

from math import pi, sqrt, hypot
from math import sin, cos
#from lookup import tableSin, tableCos as sin, cos
from random import random
import sys
from time import time

sys.setrecursionlimit(1500)
dr = 0.01
r = 2*pi/32


def main():
	start, last = time(), time()
	print("##### Random Search Results #####")
	#randomStartSearch()
	print("Time elapsed: %s"%(time() - last))
	last = time()
	print

	print("##### Uniform Search Results ####")
	#uniformSearch()
	print("Time elapsed: %s"%(time() - last))
	last = time()
	print

	print('##### Very Random Results ####')
	#veryRandomSearch()
	print("Time elapsed: %s"%(time() - last))
	last = time()
	print

	print('##### Nelder Mead Search Results ####')
	nelder_mead()
	print("Time elapsed: %s"%(time() - last))
	last = time()
	print
	print("TOTAL Time elapsed: %s"%(time() - start))

def nelder_mead():
	x, y, z = 0, 0, float('inf')

	for i in range(2):
		a = (random() * 10, random() * 10)
		b = (random() * 10, random() * 10)
		c = (random() * 10, random() * 10)
		temp = nelder_mead_recur(a, b, c)
		tx, ty = temp[0], temp[1]
		tz = f(tx,ty)
		if  tz < z:
			x, y, z = tx, ty, tz

	print("x, y, z = %s, %s, %s"%(x, y, z))


def nelder_mead_recur(a, b, c):
	b, c, a = sorted( (a, b, c), key= lambda x:f(*x) )
	orginal_a = a
	d = (b[0]+c[0]-a[0], b[1]+c[1]-a[1])
	initial = f(*a)

	if f(*d) < initial:
		e = ( -2 * a[0] + 3/2 * (b[0]+c[0]), -2 * a[1] + 3/2 * (b[1]+c[1]) )
		if f(*e) < f(*d):
			a = e
		else: 
			a = d
	else:
		fvar = (-2 * a[0] + 3/4 * (b[0]+c[0]), -2 * a[1] + 3/4 * (b[1]+c[1]))
		g = (2 * a[0] + 2 * (b[0] + c[0]), 2 * a[1] + 2 * (b[1] + c[1])  )
		if f(*fvar) < initial:
			a = f
		if f(*g) < f(*a):
			a = g
		if a == orginal_a:
			m = ( (b[0] + c[0])/2, (b[1]+c[1])/2 )
			a, b = c, m

	if dist(orginal_a, a) > 0.1 and area(a, b, c) > 0.01:
		return nelder_mead_recur(a, b, c)
	else:
		return a

def f(x, y):
	return x * sin(4*x) + 1.1*y*sin(2*y) if 0 < x < 10 and 0 < y < 10 else float('inf')

def dist(c1, c2):
	return hypot(c2[0] - c1[0], c2[1] - c1[1])

def area(a, b, c):
	return 0.1

def veryRandomSearch():
	x, y, z = 0, 0, float('inf')

	for _ in range(10000):
		tx = random() * 10
		ty = random() * 10
		tz = f(tx, ty)
		if tz < z:
			x, y, z = tx, ty, tz 

	print("x, y, z = %s, %s, %s"%(x, y, z))

def uniformSearch(maxPoints = 100):
	x, y, z = 0, 0, float('inf')
	
	for tx, ty in pointGenerator(maxPoints):
		tx, ty = search(tx, ty)
		tz = f(tx, ty)
		if tz < z:
			x, y, z = tx, ty, tz 

	z = f(tx, ty)
	print("x, y, z = %s, %s, %s"%(x, y, z))

def pointGenerator(maxPoints):
	side = sqrt(maxPoints)
	for tx in frange(0, side, 0.5):
		for ty in frange(0, side, 0.5):	
			yield tx, ty

def randomStartSearch():
	x, y, z = 0, 0, float('inf')

	for _ in range(100):
		tx = random() * 10
		ty = random() * 10
		tx, ty = search(tx, ty)
		tz = f(tx, ty)
		if tz < z:
			x, y, z = tx, ty, tz 

	print("x, y, z = %s, %s, %s"%(x, y, z))

def search(x, y):
	for t in frange(0, 2*pi, 2*pi/64):
		dx = dr * cos(t)
		dy = dr * sin(t)
		dz = f(x+dx, y+dy) - f(x, y)
		if dz < 0:
			try:
				return search(x + dx, y + dy)
			except RuntimeError:
				return x + dx, y + dy

	return x, y

def frange(start, stop, step):
	i = start
	while i < stop:
		yield i
		i += step

if __name__ == "__main__":
	main()