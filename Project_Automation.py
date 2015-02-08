import os


input = [10, 20, 50, 100, 150, 200, 300, 400, 500, 750, 1000]



print ("--5 denominations with 11 input---")
for x in range (0, 2):
	print ("---Test" + str(x+1))

	print "Dynamic Programming"
	for each in input:
		os.system("Python Dynamic_Programming.py " + str(each) + " " + "5")

	print "Brute Force"
	for each in input:
		os.system("Python Brute_Force.py " + str(each) + " " + "5")
	
print "--8 denominations with 11 input"
for x in range (0, 2):
	print "---Test" + str(x+1)

	print "Dynamic Programming"
	for each in input:
		os.system("Python Dynamic_Programming.py " + str(each) + " " + "8")

	print "Brute Force"
	for each in input:
		os.system("Python Brute_Force.py " + str(each) + " " + "8")


print "--10 denominations with 11 input"
for x in range (0, 2):
	print "---Test" + str(x+1)

	print "Dynamic Programming"
	for each in input:
		os.system("Python Dynamic_Programming.py " + str(each) + " " + "10")

	print "Brute Force"
	for each in input:
		os.system("Python Brute_Force.py " + str(each) + " " + "10")
