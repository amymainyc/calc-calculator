import matplotlib.pyplot as plt
from functions.buttons import *
from functions.calculus import *
from functions.other import *

def graph(function, *bounds):
	if bounds:
		x1, x2 = bounds[0], bounds[1]
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
	plt.show()