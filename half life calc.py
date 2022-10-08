from CUST_LIB import *

x = int(input("Input size of sample (grams): "))
halflife = float(input("Input half life of isotope (days): "))
time = 0

while x >= 1:
    x = x/2
    time = time + 1
    print(x)
print("It will take " + str(time) + " halflifes for this sample to decay below 1 gram.")
life = halflife * time
print("Thus, it will take " + str(life) + " days to decay below 1 gram.")
