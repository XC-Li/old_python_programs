#Extracting Data from JSON
import urllib
import json

url = raw_input("Enter location:")

data = urllib.urlopen(url).read()
#print data ok
input = json.loads(data)
comments = input["comments"]
print "Count:",len(comments)
sum = 0
for item in comments:
    # print item["count"]
    sum = sum + item["count"]
print sum