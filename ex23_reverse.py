import sys

script, encoding, error = sys.argv

def main(file_name, encoding, errors):
    line = file_name.readline()

    if line:
        print_line(line, encoding, errors)
        main(file_name, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    next_lang = bytes(next_lang)
    print(next_lang)

    decoded_txt = next_lang.decode(encoding, errors = errors)

    print(decoded_txt)
    # encoded_txt = decoded_txt.encode(encoding, errors = errors)

    # print(f"{decoded_txt} <===> {encoded_txt}")

# def copy_str_to_bytes(from_file, to_file, encoding):
#     from_file = open(from_file)
#     txt = from_file.read().encode(encoding)
#     to_file = open(to_file)
#     to_file.write(txt)
#     from_file.close()
#     to_file.close()
#     return to_file

language = open('lan_b.txt', encoding = encoding)

main(language, encoding, error)
