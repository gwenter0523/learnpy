print("mary had a little lamb.")
# 打印字符串，插入了变量{},用格式化方法format()插入了字符串‘snow’
print("its fleece was white as {}.".format('snow'))
print("and everywhere that mary went.")
# 打印10个*
print("." * 10) # what'd that do?

# 定义变量end1-12
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
# 拼接字符串，其中，end='   '，表示这行字符串末尾接续 几个空格‘   ’，默认情况下，每行print（）末尾是接续 \n ，即【换行】处理
print(end1 + end2 + end3 + end4 + end5 + end6, end='    ')
print(end7 + end8 + end9 + end10 + end11 + end12)