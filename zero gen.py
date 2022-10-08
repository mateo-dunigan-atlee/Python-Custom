from time import sleep

x = int(input("Number of zeroes "))
y = x

while y > 0:
    print("0")
    y = y-1
    sleep(0.001)
