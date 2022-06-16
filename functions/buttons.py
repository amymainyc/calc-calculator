from functions.calculus import *
from functions.graph import *
from functions.other import *

def sqrt(i):
  s = i[0]
  if s <= 0: 
    return "Please enter a positive value."
  x = s/2 # initial guess
  while abs(s - (x * x)) > 0.00001:
    x = (x + s/x) / 2
  return x


def fact(i):
  n = i[0]
  if n < 2:
    return 1
  return n * fact([n-1])


def sin(i):
  theta = float(i[0])
  a = pow(-1, 0) * pow(theta, 2*0+1) / fact([2*0+1])
  b = pow(-1, 1) * pow(theta, 2*1+1) / fact([2*1+1])
  sum = a + b
  n = 2
  while abs(a-b) > 0.00001:
    a = b
    b = pow(-1, n) * pow(theta, 2*n+1) / fact([2*n+1])
    sum += b
    n += 1
  return sum


def cos(i):
	theta = float(i[0])
	a = pow(-1, 0) * pow(theta, 2*0) / fact([2*0])
	b = pow(-1, 1) * pow(theta, 2*1) / fact([2*1])
	sum = a + b
	n = 2
	while abs(a-b) > 0.00001:
		a = b
		b = pow(-1, n) * pow(theta, 2*n) / fact([2*n])
		sum += b
		n += 1
	return sum


def tan(i):
	theta = i[0]
	return sin([theta]) / cos([theta])


def csc(i):
  theta = i[0]
  return 1 / sin([theta])


def sec(i):
  theta = i[0]
  return 1 / cos([theta])
  

def cot(i):
  theta = float(i[0])
  return cos([theta]) / sin([theta])


def e():
  a = 1 / fact([0]) * pow(1, 0)
  b = 1 / fact([1]) * pow(1, 1)
  sum = a + b
  n = 2
  while abs(a-b) > 0.0000001 or a-b == 0:
    a = b
    b = 1 / fact([n]) * pow(1, n)
    sum += b
    n += 1
  return sum

def e_x(i):
  x = i[0]
  return pow(e(), x)


def ln(i):
	x = i[0]
	if x <= 0:
		return "x must be > 0."
	return integral(["1/x", 1, x])
	

def log(i):
  a, b = i[0], i[1]
  if a <= 0 or b <= 0:
    return "inputs must both be positive"
  return ln([b]) / ln([a])
  # returns log of b with base a


def pi():
  # calculates pi to 5 decimal places
  a = pow(-1, 0) / (pow((2 * 0 + 3), 3) - (2 * 0 + 3))
  b = pow(-1, 1) / (pow((2 * 1 + 3), 3) - (2 * 1 + 3))
  sum = a + b
  n = 2
  while abs(a-b) > 0.000001:
    a = b
    b = pow(-1, n) / (pow((2 * n + 3), 3) - (2 * n + 3))
    sum += b
    n += 1
  return 3 + 4 * sum


def arcsin(i):
	x = float(i[0])
	if not (x <= 1 and x >= -1):
		return "x must be between -1 and 1."
	return integral(["1/((1-x**2)**0.5)", 0, x])


def arccos(i):
  x = float(i[0])
  if not (x <= 1 and x >= -1):
    return "x must be between -1 and 1."
  return pi()/2 -(arcsin([x]))

  
def arctan(i):
	x = float(i[0])
	return integral(["1/(1+x**2)", 0, x])


def arccot(i):
	x = float(i[0])
	return pi()/2 -(arctan([x]))


def arcsec(i):
  # 
	x = float(i[0])
	# this one takes a very long time 
	if not (x >= 1 or x <= -1):
		return "x must be between less than -1 or greater than 1."
	return arccos([1/x])


def arccsc(i):
  # 
	x = float(i[0])
	if not (x >= 1 or x <= -1):
		return "x must be between less than -1 or greater than 1."
	return arcsin([1/x])