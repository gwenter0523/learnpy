def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def devide(a, b):
    print(f"Deviding {a} / {b}")
    return a / b

print("let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = devide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# a puzzle for the extra credit, type ot in anyway.
print("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, devide(iq, 2))))

print("that becomes:", what, "\nCan you do it by hand?")
