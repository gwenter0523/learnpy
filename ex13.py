from sys import argv
# argv：从sys模块中导入的参数变量，保存参数
# read the wyss section for how to run this 
script, first, second, third = argv  # 解包
# 第一个参数不是用户输入的，它固定为该脚本的名称。

# python3.7 ex13.py zed yasuo lulu -> zed: 参数
# argv: 参数变量，保存着运行py脚本时传递给py脚本的参数（即zed yasuo等）

print("the script is called: ", script)
print("your first variable is ", first)
print("your second variable is : ", second)
print("your third variable is : ", third)