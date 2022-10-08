import CUST_LIB as cst

I=0
X=0

try:
  X=int(1E308)
  print("Loading complete")
  while True:
    X+=10
    X=float(X)
    if float(X)%100==0:
      print("X")
      #print(len(str(int(X))))
except OverflowError:
  cst.halt(int(X))
except KeyboardInterrupt:
  cst.halt(int(X))