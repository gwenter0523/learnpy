# 对于字典来说，key是一个字符串，获得值的语法是[key]
# 对于模块来说，key是一个函数或变量的名称，语法是 .key
# 除此之外，两者并无区别了

# 实例化的流程
# 1. 查找Mystuff()并知道他是一个被创建过的类
# 2. 创建空对象，包含所有用def定义的函数
# 3. 找‘__init__’函数，如果找得到，则用于初始化
# 4. 在__init__中，有一个多余的函数叫self

class Song(object):

    def __init__(self,lyrics, title):
        self.lyrics = lyrics
        self.title = title

    def sing(self):
        for line in self.lyrics:
            print(line)

    def say_title(self):
        print(self.title)

happy_bday = Song(["Happy birthday to you", "I do not want to get sued", "So I'll stop right there"], "happy birthday")

bulls_on_parade = Song(["They rally around the family", "With pockets full of shells"], "wtf")

happy_bday.sing()

bulls_on_parade.sing()

happy_bday.say_title()