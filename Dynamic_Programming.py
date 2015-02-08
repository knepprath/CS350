import time
import sys


def test():
	startTime = time.clock()

	target = int(sys.argv[1])
	
	
	denominations = []
	denominations = denominationSize(sys.argv[2])
	ways = [1] + [0]*target

	for bill in denominations:
		for i in range(bill, target+1):
			ways[i] += ways[i-bill]


	endTime = time.clock()

	print endTime - startTime


def denominationSize(x):
    return {
        '5': [1, 2, 5, 10, 20],
        '8': [1, 2, 5, 10, 20, 50, 100, 200],
        '10':[1, 2, 5, 10, 20, 50, 100, 200, 500, 1000],
        }.get(x, 9) 

test()