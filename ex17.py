from sys import argv
from os.path import exists

scripts, from_file, to_file = argv; 

print(f"copying from {from_file} to {to_file}")

# # we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

# len（data）可以返回传递的字符串的长度
print(f"the input file is {len(indata)} bytes long")

print(f"does the output file exist? {exists(to_file)}")
print("ready, hit RETURN to continue, ctrl+c to abort")
input('?')

out_file = open(to_file, 'w')
out_file.write(indata)

print("alright, all done")

out_file.close()
in_file.close()


# 所有代码合并成一行，用分号（；）可以做到
# from sys import argv; from os.path import exists; scripts, from_file, to_file = argv; print(f"copying from {from_file} to {to_file}"); in_file = open(from_file); indata = in_file.read(); out_file = open(to_file, 'w'); out_file.write(indata); print("alright , all done"); out_file.close(); in_file.close(); 
