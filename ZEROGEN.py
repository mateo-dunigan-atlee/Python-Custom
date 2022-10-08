import CUST_LIB as cst

def Generate(X):
  start=cst.monotonic()
  Z=float(X)
  print("0"*X)
  end=cst.monotonic()
  time=float(end-start)
  print("Execution time: "+str(round(time,3)))
  zero=float(Z/time)
  print("Number of 0s per sec: "+str(round(zero,3)))
Generate(X=int(input("Number of zeroes ")))
