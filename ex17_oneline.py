from sys import argv; scripts, from_file, to_file = argv; 
file = open(to_file, 'w').write(open(from_file).read())