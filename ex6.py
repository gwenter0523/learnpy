# 定义变量，typesofpeopple
types_of_people = 10
# 定义字符串格式化变量x，将typesofpeople放入
x = f"there are {types_of_people} types of people"

# 定义字符串变量binary和donot
binary = "binary"
do_not = "don't"
# 定义格式化字符串y，将binary和donot放入
y = f"those who know {binary} and those who {do_not}"

# 打印x和y
print(x)
print(y)

# 打印格式化字符串，分别放入了x和y
print(f"i said: {x}")
print(f"i also said: {y}")

# 定义变量hilarious和zaima
hilarious = False
zaima = "yes??"
# 定义变量joke，字符串中放入两个空的变量{}
joke_evaluation = "isn't that joke so funny?! {}{}"

# 打印joke，使用format()函数，在两个空变量中，放入了hilarious和zaima
print(joke_evaluation.format(hilarious, zaima))

w = "this is the left side of..."
e = "a string with a right side."

# 使用+拼接字符串
print(w+e)