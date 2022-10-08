import CUST_LIB as cst

II=0
try:
  X=int(float(input("Starting number\n")))
except OverflowError:
  cst.halt("Overflow")
start_time=cst.monotonic()

while X>1:
  II+=1
  I=cst.fmod(X,2)
  if I==0:
    X=X/2
  else:
    X=3*X+1

end_time=cst.monotonic()
time=round((end_time-start_time),3)
print("Time taken: "+str(round(time,3))+"s")
print("Number of iterations: " + str(II))
print("Time per iteration: "+str(round((time/II),5))+"s")
