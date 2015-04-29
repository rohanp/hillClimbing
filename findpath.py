import numpy as np

def main():
	#loading data
	f = open( 'cities.txt' ).read().splitlines()
	numCities =  f.pop(0)
	cities = []
	for line in f:
		cities.append( tuple( line.split() ) )



def getSquaredDistance(city1, city2):
	return city1[0]*city2[0] + city1[1]*city2[1]




if __name__ == "__main__":
	main()