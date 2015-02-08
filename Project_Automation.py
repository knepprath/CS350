import os


input = [10, 20, 50, 100, 150, 200, 300, 400, 500, 750, 1000]

print "Dynamic Programming"
for each in input:
	os.system("Python Dynamic_Programming.py " + str(each))

print "Brute Force"
for each in input:
	os.system("Python Brute_Force.py " + str(each))

