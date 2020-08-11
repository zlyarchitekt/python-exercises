import math

def DecimalPi(userValue):
    sp = round(math.pi, userValue)
    return sp

# Max value of decimal places
b = 20

# User's input
i = input("Please choose, how many decimal places PI should have: ")

try:
    r = int(i)
    if r > b:
        print("Please choose lower value.")
    elif r <= b:
        print(DecimalPi(r))
except:
    print("You didn't enter an integer")
