txt = input('Welcome to the Function Calcutator!\n\nThis is a calculator for determining the answers to functions of the form "f(x) = m * x + b".\n\nThe calcuator will ask for a multiplier (the "m") and an adder (the "b").\n\nTo close this press enter.')

m = float(input("\nPlease input a number for the muliplier: "))
b = float(input("\nPlease input a number for the adder: "))

def f(x):
    y = m * x + b
    return y

print("\nYour equation is:\n\n" + str(m) + " * x + " + str(b) + "\n")
print('Now type "f(x)", but replace "x" with your number.\n\nThanks for using!\n\nCredit 2021 Mateo DA and Aaron DA')
