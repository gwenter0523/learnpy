import mystuff
mystuff.apple()
print(mystuff.tangerine)
print(mystuff.mystuff['apple'])

# 创建类
class MyStuff(object):

    def __init__(self):
        # 初始化
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES")

# 类实例化（instantiate）后，称为对象（object）
thing = MyStuff()
thing.apple()
print(thing.tangerine)
