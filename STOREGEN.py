from time import *
from math import *

file=open("zeroes.txt","w")

def Generate():
  X = int(input("Number of zeroes "))
  start=monotonic()
  Z=float(X)
  while X > 0:
    file.write("0")
    X = X-1
  end=monotonic()
  time=float(end-start)
  print("Execution time: "+str(round(time,3)))
  zero=float(Z/time)
  print("Number of 0 per sec: "+str(round(zero,3)))
Generate()