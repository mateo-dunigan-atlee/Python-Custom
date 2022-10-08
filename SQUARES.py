import CUST_LIB as cst
from ti_system import *

disp_clr()
Level=0
numQ=int(float(input("How many problems do you want?\n")))
disp_clr()
total=0
start=cst.monotonic()
while numQ>=1:
  X=cst.randint(1,40)
  answer=X**2
  print("Number "+str(Level+1))
  imp=int(input("What is "+str(X)+"^2?\n"))
  if imp==answer:
    print("Correct")
    cst.sleep(0.5)
    Level=Level+1
    numQ=numQ-1
    total=total+1
    disp_clr()
  else:
    print("Incorrect\n"+str(X)+"^2="+str(answer))
    cst.sleep(2)
    total=total+1
    disp_clr()
end=cst.monotonic()
print("# correct: "+str(Level)+" out of "+str(total)+" (Accuracy: "+str((Level/total)*100)+"%)")
time=end-start
print("It took you "+str(round(time,2))+" seconds")
#print("That's "+str(round((total/time),2))+" per second")
print("That's "+str(time/total)+" seconds per problems.")