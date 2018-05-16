from sys import argv
script, filename = argv

print "We are going to erase %r." %filename
raw_input("?")
target = open(filename,'w')

print "Truncating.."
target.truncate()

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "writing file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.close()

