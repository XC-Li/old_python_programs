# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
line_list = list()
for line in handle:
    if line.startswith('From:'):
        continue
    if line.startswith('From'):
        s_line = line.split()
        line_list.append(s_line)
hrs = list()
for sample in line_list:
    # print sample
    s_l_l = sample[5].split(':')
    hrs.append(s_l_l[0])
# print hrs ok
hrs_count = dict()
for hour in hrs:
    hrs_count[hour] = hrs_count.get(hour,0) + 1
t_hrs = hrs_count.items()
# print sorted(t_hrs)
for t,c in sorted(t_hrs):
    print t,c
