fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
ori_list = list() #表示ori_list是list形式的
for line in fh:
    #print line.rstrip()
    ori_list = ori_list + line.split()
print ori_list
for word in ori_list:
    if word not in lst:
        #print word 
        lst.append(word)
lst.sort()
print lst