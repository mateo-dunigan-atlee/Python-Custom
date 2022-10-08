"""
from time import sleep

x = []
y = [0]

while True:
    print(x)
    x.append(y)
    y.append(x)
    print(y)
    sleep(1)


from time import sleep

x = (0)

while True:
    print(x)
    x = x + 1 * 2
    sleep(1)
"""

from time import sleep

repeatNumber = 0

while repeatNumber < 3:

    print("hi")

    def count_powers(limit):
        
        x = (1)
        power = (0)

        while power <= limit:
            print(x)
            print("equals 2 to the power of " + str(power))
            x = x * 2
            power = power + 1
            sleep(0.1)

        repeatNumber = repeatNumber + 1
