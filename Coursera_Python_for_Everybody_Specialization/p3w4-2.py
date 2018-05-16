#Following Links in Python
import urllib
from BeautifulSoup import *

url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Chanelle.html'
b_count = 1
while True:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    # Retrieve all of the anchor tags
    tags = soup('a')
    s_count = 0
    for tag in tags:
       link = tag.get('href', None)
       s_count = s_count + 1
       if s_count == 18:
            break
    print link
    url = str(link)
    b_count = b_count +1
    if b_count == 8:
        break