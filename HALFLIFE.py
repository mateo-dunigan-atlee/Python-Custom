x=float(input("Input size of sample (grams): "))

if input("Does the sample have a halflife measured in days(d) or years(y)?"=="d"):
  halflife=float(input("Input half life of isotope (days): "))
else:
  halflife = float(input("Input half life of isotope (years: )"))

time=0

while x>=1:
  x=x/2
  time+=1
print("It will take " + str(time) + " halflifes for this sample to decay below 1 gram.")
life=halflife*time
if life<365:
  print("Thus, it will take " + str(int(life)) + " days to decay below 1 gram.")
else:
  print("Thus, it will take " + str(int(life/365)) + " years to decay below 1 gram.")