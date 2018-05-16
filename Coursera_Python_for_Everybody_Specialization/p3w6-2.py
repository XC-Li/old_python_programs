#Calling a JSON API
import urllib
import json
import os
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

address = raw_input("Enter Location:")
url = serviceurl + urllib.urlencode({'sensor':'false','address':address})

print 'Retriving',url
data = urllib.urlopen(url).read()
print 'Retrieved',len(data),'characters'

js = json.loads(str(data))
# print json.dumps(js, indent=4)
print js['results'][0]['place_id']