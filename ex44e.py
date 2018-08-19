# 组合

# 调用模块里的函数，实现直接使用别的类和模块

class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")


class Child(object):
    
    def __init__(self):
        # 创建一个属性，赋值。值为Other类的一个实例
        self.other = Other()

    def implicit(self):
        # 直接使用Other里的方法
        self.other.implicit()

    def override(self):
        # 自己本身的方法，虽然同名，但跟Other中的override没有关系
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        # 调用other类的altered方法
        self.other.altered()
        print("CHILD, BEFORE OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()