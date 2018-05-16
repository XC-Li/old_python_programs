# part3-week2
#  In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
import re
# filename = raw_input('input:')
filename = 'regex_sum_174859.txt'
file = open(filename)
sum = 0
for line in file:
    number = re.findall('[0-9]+', line)
    for n in number:
        sum = sum + int(n)
print sum