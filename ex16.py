# close() 关闭文件，且保存
# read()，读取文件的内容，可以吧结果付给一个变量
# readline，只读取文本文件的一行
# trucate，清空文件
# write（‘stuff’），将stuff写入文件
# seek（0）将读写位置移动到文件开头

# 来写一个文本编辑器吧！

from sys import argv

# 文件名传参进来
script, filename = argv

print(f"we're going to erase {filename}.")
print("if you don't want that, hit ctrl+c (^c)")
print("if you do want that, hit return")

input("?")

print("opening the file...")

# 打开文件
# 给open多传递一个‘w’，表示需要往这个文件写入一些东西，如果不穿，open默认为只读
# ‘w’表示写入模式，‘r’表示读取，‘a’表示追加（append）
target = open(filename, 'w')

print("truncating the file. goodbye!")

# 清空文件
# target.truncate()

print("now i'm going to ask you for three lines.")

# 用户输入三行文字
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("i'm going to write these to the file")

# 写入用户录入的3行文字
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
target.write(f"{line1}\n{line2}\n{line3}\n")

# 关闭并保存文件
print("and finally, we close it.")
target.close()