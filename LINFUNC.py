import ti_plotlib as plt
from ti_system import *

print("A program for functions of form mx+b. \nWill prompt for m, x, and b. \nCan be called from shell with f(X).\nPress [clear] to continue.")
disp_wait()
def f(x):
  x=int(x)
  a=int(input("m: "))
  b=int(input("b: "))
  y=a*x+b
  x1=x
  x2=x*2
  y1=y
  y2=y*2
  plt.cls()
  plt.window(-10,10,-10,10)
  plt.labels("X","Y",12,2)
  plt.grid(1,1,"dot")
  plt.axes("on")
  plt.color(1,1,1)
  plt.line(x1,y1,x2,y2,"")
  plt.show_plot()
