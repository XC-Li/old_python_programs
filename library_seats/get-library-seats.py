# get library seats
# Designed By Xc.Li
import urllib
import BeautifulSoup
import re
import time
from os import system

import kol
import writetocsv
import timer


def find_number(keyword):
    for tag in tags:
        s_tag = str(tag)
        flag = re.match(keyword, s_tag)
        if flag is not None:
            return s_tag[54:-18]

while True:
    timer.func(10)
    kol.func()
    url = 'http://lib.ecust.edu.cn:8081/gateseat/lrp.aspx'
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup.BeautifulSoup(html)
    tags = soup('span')

    output = list()
    output.append(time.ctime()[11:-5])
    # time in decimal
    hour = int(time.ctime()[11:13])
    minute = int(time.ctime()[14:16])
    decimal_time = round(hour + minute/60.0, 2)
    output.append(decimal_time)

    for floor in [1, 2, 3, 4, 5, 6]:
        # print 'Floor:', floor
        keyword = '^<span id="Label' + str(floor) + 'f1' + '".*>'
        # print 'Used:', find_number(keyword)
        output.append(int(find_number(keyword)))
        keyword = '^<span id="Label' + str(floor) + 'f2' + '".*>'
        # print 'Left:', find_number(keyword)
        output.append(int(find_number(keyword)))
    print output
    str_output = str(output)[1:-1]
    writetocsv.write('lib', 'default', str_output)
    time.sleep(60)
    system('cls')
    # auto-quit
    if hour == 22 and minute > 29:
        print "program ends!"
        writetocsv.write('lib', 'default', "program end at:%s" % time.ctime())
        time.sleep(5)
        break
