import time
import sys



def test():
	target = int(sys.argv[1])
	ways = 0

	startTime = time.clock()

	if (sys.argv[2] == "5"):
		d = target
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

	if (sys.argv[2] == "8"):
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
		
	if (sys.argv[2] == "10"):
		z = target
		while (z >= 0):
			x = z
			while (x >= 0):
				a = x
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
				x -= 500
			z -= 1000

	endTime = time.clock()

	print endTime - startTime
							
test()			
				