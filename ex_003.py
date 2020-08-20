# Fibonacci Sequence

def fib():
    i = 0
    a = int(input("Please give a first value: "))
    n = int(input("Please give a second value: "))
    print(f"Your Fibonacci Sequence starts with: {a}")
    b = a
    print(b)

    while i < n:
        c = a + b
        a = b
        b = c
        print(b)
        i += 1
    else:
        print("Thank you for a great fun!")

print("Fibonacci Sequence")
print("You can input a two values. First value is the beginning of the Sequence. Second is number of operations")

fib()
