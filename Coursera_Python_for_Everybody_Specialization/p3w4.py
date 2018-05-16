#Scraping Numbers from HTML using BeautifulSoup
import urllib
from BeautifulSoup import *
import re
url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_174864.html'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
sum = 0
tags = soup('span')
for tag in tags:
    print tag
    tag = str(tag)
    number = re.findall('[0-9]+',tag)
    for n in number:
        sum = sum + int(n)
print sum