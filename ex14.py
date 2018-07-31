from sys import argv
script, user_name = argv
prompt = '>> '

print(f"hi {user_name}, i'm the {script} script")
print("i'd like to ask you a few quewtions.")
print(f"do you like me {user_name}")
likes = input(prompt)
# input（参数）的效果是：输入时，会提示括号里的参数内容，如输入了">"
# 则输入时会在前面加上 >

print(f"where do you live {user_name}")
lives = input(prompt)

print(f"what kind of computer do you have?")
computer = input(prompt)

print(f"""
alright so you said {likes} about liking me.
you live in {lives}. not sure where where that is.
and you have a {computer} computer. nice.
""")
