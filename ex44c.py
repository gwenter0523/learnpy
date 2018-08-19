# 在运行前或运行后替换
# 首先覆盖父类的函数，然后用super()来调用父类的版本

class Parent(object):

    def altered(self):
        print("PARENT altered()")


class Child(Parent):
    
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()

# 事实上执行的仍然是Child内的函数，但在函数内（第14行）用到了super()，调用了一次父类中的altered函数
dad.altered()
son.altered()