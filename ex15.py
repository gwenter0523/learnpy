from sys import argv

script, filename = argv

txt = open(filename)    # 不是写死的文件名，是用户输入的参数
# 将filename文件赋值给txt。
# open（）：接受一个参数，返回一个值，这就是打开文件的过程
# 注意，open（）返回的不是文件的内容，返回的是一个叫“文件对象”（file object）的东西

print(f"here is your file {filename}")
print(txt.read())
# var.read() 读取var文件里的内容。执行read命令、。

txt.close()
# 关闭文件也很重要

print("type the file name again: ")
file_again = input(">")
# 输入file_again的值

txt_again = open(file_again)
# 打开file_again文件，赋值给txt_again

print(txt_again.read())
# 打印出txt_again的读取内容

txt_again.close()