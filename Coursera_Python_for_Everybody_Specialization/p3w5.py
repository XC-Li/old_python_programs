import urllib
import xml.etree.ElementTree as ET

serviceurl = str(raw_input('Enter Location:'))
# serviceurl = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_174861.xml"
print 'retriving' ,serviceurl
rawxml = urllib.urlopen(serviceurl).read()
print 'retrivied',len(rawxml),'characters'
# print rawxml
tree = ET.fromstring(rawxml)
counts = tree.findall('.//count')
# print tree.tag
print 'count:',len(counts)
sum = 0
for comments in tree:
    # print comments.tag
    for comment in comments:
        # print comment.tag
        name = comment.find('name').text
        # print name
        count = comment.find('count').text
        # print count
        sum = sum + int(count)
print 'sum:',sum