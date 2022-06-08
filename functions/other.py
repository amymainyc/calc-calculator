from functions.buttons import *
from functions.calculus import *
from functions.graph import *

def mean(arr):
  sum = 0
  for i in arr:
    sum += i
  return sum / len(arr)

def median(arr):
  mid = int(len(arr) / 2) - 1
  if len(arr) % 2 == 0:
    return (arr[mid] + arr[mid + 1]) / 2
  else:
    return arr[mid + 1]

def mode(arr):
  d = {}
  for i in arr:
    if not i in d.keys():
      d.update({i: 0})
    d[i] += 1
  mxKey = 0
  mxVal = 0
  for i in d.keys():
    if d[i] > mxVal:
      mxKey = i
      mxVal = d[i]
  return mxKey

def range(arr):
  max = arr[0]
  min = arr[0]
  for i in range(len(arr)):
    max = max(max, arr[i])
    min = min(min, arr[i])
  return max - min

def sigma(func, a, b):
  sum = 0
  for i in range(a, b+1):
    x = i
    sum += eval(func)
  return sum

def primeFact(n):
  arr = []
  while n > 1:
    i = 2
    while i<=n:
      if (n/i) % 1 == 0:
        arr.append(i)
        n /= i
        break
      i+=1
  return arr
        

def lcm(a, b):
  prod = abs(a * b)
  return prod / gcd(a, b)
  

def gcd(a, b):
  big = max(a, b)
  small = min(a, b)
  if big % small == 0:
    return small
  else:
    gcd = 1
    remainder = big % small
    while big > remainder:
      gcd *= remainder
      big /= small
  return gcd

def nPr(n, r):
  # returns number of permutations based on a sample of r elements from a set of size n
  return fact(n) / fact(n - r)

def nCr(n, r):
  # returns number of unique permutations
  return (fact(n) / (fact(r) * fact(n - r)))
          

def fact(n):
  if n < 2:
    return 1
  return n * fact(n-1)

def sqrt(s):
  if s <= 0: 
    return "Please enter a positive value."
  x = s/2 # initial guess
  while abs(s - (x * x)) > 0.00001:
    x = (x + s/x) / 2
  return x
  

def distance(x1, y1, x2, y2):
  return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

