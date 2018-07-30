name = 'Zed A. shaw'
age = 35 # not a lie
my_height = 74 # inches
height = my_height * 2.2
my_weight = 180 # lbs
# round()函数，将浮点数四舍五入
weight = round(my_weight / 1.875)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"he's {height} inches tall.")
print(f"he's {weight} pounds heavy")
print("actually that's not too heavy")
print(f"he is got {eyes} eyes and {hair} hair.")
print(f"his heeth are usually {teeth} depending on the coffee")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"if i add {age}, {height}, and {weight} i get {total}")