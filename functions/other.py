from functions.buttons import *
from functions.calculus import *
from functions.graph import *


def mean(arr):
  sum = 0
  for i in arr[:-1]:
    # last element is ''
    sum += float(i)
  return sum / (len(arr)-1)


def median(arr):
  arr = arr[:-1]
  arr.sort()
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


def range2(arr):
  arr = arr[:-1]
  arr.sort()
  mx = arr[0]
  mn = arr[0]
  for i in range(len(arr)):
    mx = max(mx, arr[i])
    mn = min(mn, arr[i])
  return mx - mn


def sigma(i):
  func, a, b =  i[0], i[1], i[2]
  sum = 0
  for i in range(a, b+1):
    sum += eval(func)
  return sum


def primeFact(i):
  n = i[0]
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
        

def lcm(i):
  a, b = i[0], i[1]
  prod = abs(a * b)
  return prod / gcd([a, b])
  

def gcd(i):
  a, b = i[0], i[1]
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


def nPr(i):
  n, r = i[0], i[1]
  # returns number of permutations based on a sample of r elements from a set of size n
  return fact(n) / fact(n - r)


def nCr(i):
  n, r = i[0], i[1]
  # returns number of unique permutations
  return (fact(n) / (fact(r) * fact(n - r)))
  

def distance(i):
  x1, y1, x2, y2 = i[0], i[1], i[2], i[3]
  return sqrt([(x1 - x2) ** 2 + (y1 - y2) ** 2])

