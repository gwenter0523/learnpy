# while loop


def while_loop(x, y):
    i = 0
    numbers = []
    while i < x:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += y
        print("\tNumbers now: ", numbers)
        print(f"At the bottom i is {i}")

    return numbers

numbers = while_loop(6, 2)

print("The numbers: ")
for num in numbers:
    print(num)
