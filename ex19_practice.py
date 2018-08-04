from sys import argv
script, first, second, filename = argv

# 定义函数，实现的功能是使传入的参数相加
def plus_func(a,b):
    print(int(a) + int(b))

# 1
print("第1种")
plus_func(1, 2)

# 2
print("第2种")
plus_func(first, second)

# 3
print("第3种")
a = 1
b = 2
plus_func(a, b)

# 4
print("第4种")
plus_func(a + 2, b - 6)

# 5
print("第6种")
plus_func(a + int(first), int(second))

# 6
print("第6种")
c = input("input a number here:")
c = int(c)
plus_func(a, c)

# 7
print("第7种")
plus_func(c + b, a)

# 8
print("第8种")
plus_func(c-20, a + b)

# 9 输入浮点数，把它round
print("第9种")
d = input("input a float: ")
d = float(d)
plus_func(round(d), a)

# 10 读取txt中的数字
print("第10种")
txt_num = open(filename).readline()
plus_func(txt_num, a)