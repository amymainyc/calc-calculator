import matplotlib.pyplot as plt
from functions.buttons import *
from functions.calculus import *
from functions.other import *
import random

def graph(i):
	# plt.ioff()
	print(i)
	function, bounds = i[0], i[1:]
	if bounds[0] != " ":
		print(bounds)
		x1 = bounds[0]
		x2 = bounds[1]
	else:
		x1, x2 = -10, 10

	x_list = []
	y_list = []
	interval = (x2-x1)/100
	for i in range(101):
		x = x1 + (i*interval)
		x_list.append(x)
		y_list.append(eval(function))
	plt.plot(x_list, y_list)
	id = random.randint(100000, 999999)
	plt.savefig(f"static/{id}.png")
	plt.close()
	return f'<img src="static/{id}.png" height="600" alt="' + function + '"><br>'

# plt.show()