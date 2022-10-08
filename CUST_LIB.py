from math import *
from random import *
from time import *
import sys as sys

def fact(X):
  int(float(X))
  y=range(X)
  z=1
  for i in y:
    z=z*(X-i)
  return int(z)

def addFact(X):
  int(float(X))
  y=range(X)
  z=0
  for i in y:
    z=z+(X-i)
  return int(z)

def randList(X):
  R=[]
  for i in range(X):
    R.append(randint(0,10))
  return R

def allFactors(X):
  factors=[]
  for i in range(1,int(sqrt(abs(X))+1)):
    Y=X/i
    if float(Y)-int(Y)==0:
      factors.append(int(Y))
  for i in range(len(factors)):
    Z=factors[i]
    factors.append(int(X/Z))
  factors=sorted(factors)
  factors.remove(1)
  factors.remove(X)
  return factors

def keyFinder(X):
  #Keys for Greek cipher
  Y=[]
  count=0
  bigI=0
  n=[]
  for i in range(1,X):
    n=allFactors(i)
    if len(n)>=count:
      count=len(n)
      Y=n
      bigI=i
  return Y,bigI

def sumation(j,n,func):
  #start,stop,"function"
  func=str(func)
  total=[]
  r=range(j,n+1,1)
  for i in r:
    total.append(eval(func,{"n":n},{"i":i}))
  return int(sum(total))

