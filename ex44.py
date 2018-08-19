# 大部分使用继承的场合都可以使用组合取代或简化。
# 多重继承指的是我们定义的类继承了一个或多个类。如 class SuperFun(Child, BadStuff)
# 一定要尽量避免多重继承

# 继承指的是一个类的大部分或全部功能都是从一个父类中取得的

# 通过组合的方式，也能实现，直接使用别的类和模块的目的

# 继承
class Parent(object):
    pass

class Child(Parent):
    pass

# 组合
class Other(object):
    def oter_method(self):
        pass

class Another(object):
    def __init__(self):
        # 定义一个属性，赋值。值为另一个类的实例
        self.other = Other()

    def altered(self):
        # 可以直接通过这个属性，调用其他类或模块中的方法
        self.other.oter_method()

# 继承和组合都是为了解决代码复用的问题

# 几个原则：
#   1. 不惜一切代价避免【多重继承】
#   2. 如果只是有一些代码会在不同位置和场合用到，就用组合来把它们做成模块
#   3. 只有在代码的可复用部分之间有清楚的关联，可以通过一个单独的共性联系起来，才使用继承，或者非使用继承不可的场合

# pyehon中，类更像是用来创建对象（实例）的模板。就像制作硬币的模具一样。
