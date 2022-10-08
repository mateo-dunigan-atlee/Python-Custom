from CUST_LIB import *

print("A program for solving quadratics of form ax^2+bx+c. \nOutputs a value for x in standard form. \nUses the quadratic formula. \nPrompts for a, b, and c. \nRun with [vars]=> Solve().")

def Solve():
  a=int(input("a: "))
  b=int(input("b: "))
  c=int(input("c: "))
  r=(b**2)-(4*a*c)
  try:
    root=sqrt(r)
  except ValueError:
    resp=input("WARNING: Negative radicand. Continue with complex numbers?\ny/n\n")
    if resp=="y":
      root=negRad(r)
    else:
      sys.exit()
  X1=((-b+root)/(2*a))
  X2=((-b-root)/(2*a))
  if -X1==X2:
    print("X=+/-"+str(X1))
  elif X1==X2:
    print("X="+str(X1))
  else:
    print("X= "+str(X1)+", "+str(X2))

def negRad(X):
  X=sqrt(abs(X))
  i=complex(0,1)
  X=X*i
  return X

Solve()