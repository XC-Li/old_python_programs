# 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counter = dict()
namelist = list()
for line in handle:#checking every line
    line = line.rstrip()
    if line.startswith('From:'):
        continue
    if line.startswith('From'):
        s_line = line.split()
        # print line ok
        namelist.append(s_line[1])
# print namelist
for names in namelist:
    counter[names] = counter.get(names,0) + 1
# print counter

big_count = None
big_name = None
for name,count in counter.items():
    if big_count is None or count > big_count:
        big_name = name
        big_count = count
print big_name,big_count