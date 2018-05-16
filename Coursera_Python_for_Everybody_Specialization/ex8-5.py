fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
looking = raw_input("看什么:")

fh = open(fname)
count = 0
for line in fh:
    if line.startswith('From:'):
        continue
    if line.startswith(looking):
        word = line.split()
        print word[1]
        count = count + 1
print "There were", count, "lines in the file with From as the first word"
