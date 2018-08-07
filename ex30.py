# else if

people = 30
cars = 40
trucks = 15

if cars > people:
    print("we should take the cars.")
elif cars < people:
    print("we should not take the cars.")
else:
    print("We can not decide")

if trucks > cars:
    print("That is too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can not decide.")

if people > trucks:
    print("Alright, let us just take the trucks.")
else:
    print("Fine, let us stay home then.")
