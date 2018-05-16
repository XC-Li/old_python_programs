#word counting program 
#Designed By Xc Li
#Oct. 2015
#coding:utf-8
import os
print 'Instructions:\n1.Only support txt files\n2.Name filename in English\n3.Put the file to be analysed and this program in the same folder\nHave Fun:)'
file_name = raw_input("File name:")
try:
    fh = open(file_name)
except:
    print "Error"
sentence = list()
for line in fh:
    #print line ok
    line = line.strip()
    line = line.replace('!','.')
    se = line.split('.')
    sentence.append(se)
# print sentence 
count = 1
s_list = list()
for s in sentence:
    for s_1 in s:
        words = s_1.split()
        s_1 = str(len(words))+' '+s_1
    # print s 
        if len(words) > 0:
            s_list.append(s_1)
    # print s_list
        
s_list.sort()
for s in s_list:
    print s
print 'Done!'
os.system("pause")