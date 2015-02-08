import time
import sys

target = int(sys.argv[1])
ways = 0

startTime = time.clock()

a = target
while (a >= 0):
	b = a
	while (b >= 0):
		c = b
		while (c >= 0):
			d = c
			while (d >= 0):
				e = d
				while (e >= 0):
					f = e 
					while (f >= 0):
						g = f
						while (g >= 0):
							ways += 1
							g -= 2
						f -= 5
					e -= 10
				d -= 20
			c -= 50
		b -= 100
	a -= 200

endTime = time.clock()

print endTime - startTime
							
				
				