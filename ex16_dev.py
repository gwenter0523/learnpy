from sys import argv

script, filename = argv

print(f"well, let's write something in {filename}")

# open file with append mode
target = open(filename, 'r')


# input some words
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")


# write those words into the file
target.write(f"{line1}\n{line2}\n{line3}\n")

# close file
target.close()