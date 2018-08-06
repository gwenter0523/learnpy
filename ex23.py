import sys
script, encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    # strip()? 删掉每一行的\n而已
    next_lang = line.strip()
    # 将传入的txt中的一行string编码成原始字节，用encode方法获取原始字节串
    # DBES decode bytes，encode string
    raw_bytes = next_lang.encode(encoding, errors = errors)
    # 额外的一步，展示了encode的逆操作，decode。解码encode后的字符串（string）
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    # print(raw_bytes, "<===>", cooked_string)
    print(f"{raw_bytes} <===> {cooked_string}")

languages = open("languages.txt", encoding = "utf-8")

main(languages, encoding, error)
