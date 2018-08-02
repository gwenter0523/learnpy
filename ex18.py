# this one is like your scripts with argv

# 首先，用def命令创建一个函数，即“定义”define
# 紧挨着是函数的名字
# 括号内，告诉函数，需要*args参数
# 接着用冒号(:)结束这一行
# python可以跳过参数解包的过程，直接用括号内传入的参数作为变量名

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1:  {arg1}, arg2: {arg2}")

# ok that *args is actually pointless , we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1:  {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no argument
def print_none(): 
    print("i got nothing.")

print_two("zed", "shaw")
print_two_again("Zed", "shaw")
print_one("first!")
print_none()