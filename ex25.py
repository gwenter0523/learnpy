# 定义函数时，放在"""之间的字符串，被称为帮助文档，或文档注释
# 使用help(ex25)或help(ex25.break_word)可以查看"""的内容

def break_words(stuff):
    # 按照空格分割一个字符串
    """This function will break up words fo us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    # 排序，默认按首字母升序排列
    """sorts the words"""
    return sorted(words)

def print_first_word(words):
    # 得到数组中第一个，并从数组中去掉它
    # arr.pop(n)，从数组中去除第n个，并返回它
    '''print the first word after popping it off'''
    word = words.pop(0)
    print(words)
    print(word)

def print_last_word(words):
    '''print the last word after popping it off'''
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Take in a full sentence and return the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


