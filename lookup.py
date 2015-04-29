__author__ = "Rohan Pandit"

from math import sin, cos, pi
import pickle as pkl

sinTable = pkl.load( open('sin.pkl', 'r') )
cosTable = pkl.load( open('cos.pkl', 'r') )

def tableSin(z):
	return sinTable[ round(z%(2*pi), 1) ]

def tableCos(z):
	return cosTable[ round(z%(2*pi), 1) ]

def calcTable():
	sinTable = {}
	cosTable = {}

	for z in frange(0, 2*pi+0.1, 0.1):
		sinTable[ round(z, 1) ] = sin(z)
		cosTable[ round(z, 1) ] = cos(z)

	pkl.dump(sinTable, open('sin.pkl', 'w'), 1)
	pkl.dump(cosTable, open('cos.pkl', 'w'), 1)

def frange(start, stop, step):
	i = start
	while i < stop:
		yield i
		i += step

