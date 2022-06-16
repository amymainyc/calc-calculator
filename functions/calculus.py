from functions.buttons import *
from functions.graph import *
from functions.other import *
#:D
def derivative(i):
  function, x = i[0], i[1]
  h = 0.0000000000001
  return (eval(function.replace("x", "(x+h)")) - eval(function)) / h


def integral(i):
	function, x1, x2 = i[0], i[1], i[2]
	intervals = 10
	sum1 = reimannSum([function, x1, x2, intervals, "m"])
	intervals += 10
	sum2 = reimannSum([function, x1, x2, intervals, "m"])
	while abs(sum2-sum1) > 0.00001:
		sum1 = sum2
		intervals += 10
		sum2 = reimannSum([function, x1, x2, intervals, "m"])
	return sum2


def reimannSum(i):
	function, x1, x2, intervals, lrm = i[0], i[1], i[2], i[3], i[4]
	if x1 == x2:
		return 0
	lrm = lrm[0]
	points = []
	interval_size = (x2-x1)/intervals
	for i in range(intervals):
		if lrm == "l":
			points.append(interval_size * i + x1)
		elif lrm == "r":
			points.append(interval_size * (i+1) + x1)
		elif lrm == "m":
			points.append(interval_size * i + x1 + interval_size/2)
		else:
			return "Please specify l, r, or m for left, right, or midpoint reinmann sum."
	sum = 0
	for x in points:
		sum += eval(function) * interval_size
	return sum


def trapezoidSum(i):
	function, x1, x2, intervals = i[0], i[1], i[2], i[3]
	if x1 == x2:
		return 0
	points = [x1]
	interval_size = (x2-x1)/intervals
	for i in range(intervals):
		points.append(interval_size * (i+1) + x1)
	sum = 0
	for i in range(len(points)-1):
		x = points[i]
		y1 = eval(function)
		x = points[i+1]
		y2 = eval(function)
		sum += (y1+y2)/2 * interval_size
	return sum


def euler(i):
	dFunction, x, y, stepsize, predictX = i[0], i[1], i[2], i[3], i[4]
	while (x < predictX):
		change = eval(dFunction)
		y += change * stepsize
		x += stepsize
	return y


def minVal(i):
	function, lo, hi = i[0], i[1], i[2]
	x = lo
	mn_x = lo
	mn_y = eval(function)
	while x <= hi:
		if mn_y > eval(function):
			mn_x = x
			mn_y = eval(function)
		x += 0.001
		x = round(x, 7)
	return [mn_x, mn_y]


def maxVal(i):
  function, lo, hi = i[0], i[1], i[2]
  x = lo
  mx_x = lo
  mx_y = eval(function)
  while x <= hi:
    if mx_y < eval(function):
      mx_x = x
      mx_y = eval(function)
    x += 0.001
    x = round(x, 7)
  return [mx_x, mx_y]


def findZeroes(i):
  function, lo, hi = i[0], i[1], i[2]
  x = lo
  zeroes = []
  while x <= hi:
    fz = eval(function)
    if fz == 0:
      zeroes.append(x)
    x += 1
  return zeroes

  
#doesn't always work when there are multiple intervals;-;
def intervalInc(i):
  function, lo, hi = i[0], i[1], i[2]
  x = lo
  test = []
  print(eval(function.replace("x", "(x + 0.01)")))
  while x <= hi:
    if eval(function.replace("x", "(x + 0.01)")) > eval(function): 
      test.append(x)
    x += 0.001
  interval = []
  interval.append(test[0])
  interval.append(test[len(test) - 1])
  for i in range (len(test) - 1):
    if abs(test[i+1] - test[i]) > 0.002:
      interval.append(test[i])
  interval.sort()
  return interval


def intervalDec(i):
  function, lo, hi = i[0], i[1], i[2]
  x = lo
  test = []
  print(eval(function.replace("x", "(x - 0.01)")))
  while x <= hi:
    if eval(function.replace("x", "(x - 0.01)")) > eval(function): 
      test.append(x)
    x += 0.001
  interval = []
  interval.append(test[0])
  interval.append(test[len(test) - 1])
  for i in range (len(test) - 1):
    if abs(test[i+1] - test[i]) > 0.002:
      interval.append(test[i])
  interval.sort()
  return interval

  
#only works if the intersections are whole numbers
def findInter(i):
  function1, function2, lo, hi = i[0], i[1], i[2], i[3]
  x = lo
  inter = []
  while x <= hi:
    f1 = eval(function1)
    f2 = eval(function2)
    if f1 == f2:
      inter.append(x)
    x += 1
  return inter