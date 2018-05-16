#LPHW ex15
# from sys import argv
import sys
script, filename = sys.argv
txt = open(filename)

print "Here is your file %r:" %filename
print txt.read()
txt.close()
print "Type in the file name again:"
file_again = raw_input(">")
txt_again = open(file_again)
print txt_again.read()
txt_again.close() 