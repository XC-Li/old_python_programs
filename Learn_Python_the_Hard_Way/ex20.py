#ex20

from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()
    
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    line = f.readline().strip()
    print line_count, line, len(line)
    
current_file = open(input_file)


print_all(current_file)

rewind(current_file)

for i in [1, 2, 3]:
    print_a_line(i,current_file)
    