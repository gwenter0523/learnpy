import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):": "Make a class named %%% that is-a %%%",
    "class %%%(object): \n\tdef __init__(self, ***)": "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object): \n\tdef ***(self, @@@)": "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()": "Set *** to an instance of class %%%.",
    "***.***(@@@)": "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'": "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASES_FIRST = True
else:
    PHRASES_FIRST = False

# load up the word feom the website
# urlopen(URL) 打开URL
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding = "utf-8"))

def convert(snippet, phrase):
    # 做一个classname和参数name的数组出来
    # 从WORDS中随机获取“snippet里的%%%总数”个元素，并处理为首字母大写
    # random.sample(list,5) 从list中随机获取5个元素，作为一个片段返回
    class_name = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    other_name = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_coount = random.randint(1, 3)        
        param_names.append(', '.join(random.sample(WORDS, param_coount)))

    for sentence in snippet, phrase:
        # 复制整个数组，for s in s，p 表示s遍历s和p
        result = sentence[:]

        # fake class names
        for word in class_name:
            # 用随机生成的class name替换掉%%%
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_name:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        # random.shuffle(list)，给list里的项目随机排序 
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASES_FIRST:
                question, answer = answer, question

        print(question)

        input("> ")
        print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")