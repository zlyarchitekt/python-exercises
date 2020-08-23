# Find PI to the Nth Digit
# Enter a number and have the program
# generate PI up to that many decimal places.
# Keep a limit to how far the program will go.

import math

# Border oof decimal places
b = 15


def DecimalPi(userValue):
    sp = round(math.pi, userValue)
    return print(f"Your result: {sp}")


# User's input
i = input("Please choose how many decimal places PI should have: ")

try:
    r = int(i)
    if r > b:
        print("Please choose lower value.")
    elif r <= b:
        DecimalPi(r)
except ValueError:
    print("You didn't enter an integer")
