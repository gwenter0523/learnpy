formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format('one', 'two', 'three', 'four'))
print(formatter.format(True, False, False, True))
# 为每个{}填入formatter自身，即{} {} {} {} * 4
print(formatter.format(formatter, formatter, formatter, formatter))
# 格式化字符串，为每个{}填入字符串
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

# 这个习题中，用到了函数（function）