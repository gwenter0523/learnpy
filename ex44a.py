# 隐式继承
# 父类定义了一个函数，而子类中没有定义

class Parent(object):

    def implicit(self):
        print("PARENT implicit()")


class Child(Parent):
    pass

dad = Parent()
son = Child()

# 子类可以完全继承父类的方法。自动获得这些函数功能，可以通过这样避免大量的重复代码
dad.implicit()
son.implicit()