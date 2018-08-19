# 显式继承
# 子类的同名函数，与父类有不同的功能，可以覆盖它

class Parent(object):

    def override(self):
        print("PARENT override()")


class Child(Parent):

    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

# 子类的同名函数会覆盖父类的函数。取代了他
dad.override()
son.override()