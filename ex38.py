# 列表的操作。
# python里，调用某个class的实例的函数，看上去是 a.test(b)
# 事实上是test(a, b)

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding", next_one)
    stuff.append(next_one)

print("There we go: ", stuff)

print("Let's do some things with stuff")

# 打印数组第2项
print(stuff[1])
# 打印数组最后一项
print(stuff[-1])
# 删除数组最后一项，并返回，打印出来
print(stuff.pop())
# 往数组每项之间插入‘ ’，变成一个字符串
print(' '.join(stuff))
# 往数组第4和第5位之间插入#，变成一个字符串
print('#'.join(stuff[3:5]))
