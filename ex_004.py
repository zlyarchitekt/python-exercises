# Prime factorization
# Have the user enter a number and find all Prime Factors (if there are any) and display them.

primefactor = []

# Check input
def prime_factor():
    if number > 1:
        for x in range(2, number):
            if number % x == 0:
                checker()
                break
        else:
            print("Your input is a prime number.")
    elif number == 0:
        print(f"Your input is a {number}.")
    elif number == 1:
        print(f"Your input is a {number}.")


# Check Prime Factor
def checker():
    i = 1

    while i <= number:
        k = 0
        if number % i == 0:
            # part below need upgrade
            j = 1
            while j <= i:
                if i % j == 0:
                    k += 1
                j += 1
            if k == 2:
                primefactor.append(i)
        i += 1
    print(primefactor)

# Have the user enter a number.
value = input("Enter an integer: ")
try:
    number = int(value)
    print(f"You input {number}. Prime factor/s: ")
    prime_factor()
except ValueError:
    print("No, input is not a number. It's a string.")
