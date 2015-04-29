from math import sin, cos, pi
import pickle as pkl


def frange(start, stop, step):
	i = start
	while i < stop:
		yield i
		i += step

sinList = []
cosList = []

for i in frange(0, 2*pi, 2*pi/32):
	sinList.append( sin(i) )
	cosList.append( cos(i) )

pkl.dump(sinList, open('sinlist.pkl', 'w'))
pkl.dump(cosList, open('cosList.pkl', 'w'))