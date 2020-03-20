#XMl and JSON are two markup languages that serve as intermediaries
#b/w python data and other data across the web

#XML = Extensible Markup Language

#Xsd = schema format for XML schema


# parsing XMl

import xml.etree.ElementTree as ET data = '''
<person>
    <name > Chuck </name>
    <phone type ="intl">
+ 1 734 303 4456
</phone>
<email hide ="yes"/>
</person>'''

tree = ET.fromstring( data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

#Looping through nodes
import xml.etree.ElementTree as ET
input = '''
<stuff>
    <users>
        <user x ="2">
            <id> 001 </ id >
            <name> Chuck </ name >
        </user>
        <user x ="7">
            <id> 009 </id>
            <name> Brent </name>
        </user> </users> </stuff>'''
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print(' User count:', len( lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))

#next up JSON
#JSON is much more simplifiede
#JSOn is in the middle between JSOn and Javascript
#JSOn is basically a series of nested lists and dictionaries

import json
data = '''
[
    {"id" : "001",
     "x" : "2",
     "name" : "Chuck"
      } ,
    { "id" : "009",
     "x" : "7",
      "name" : "Chuck"
      } ]'''
info = json.loads(data)
print('User count:', len(info))
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item[ x'])

#https://www.py4e.com/code3/json2.py
import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])



#13.8 Securing API requests
#Google then Twitter API

#Code: http://www.py4e.com/code3/geojson.py

import urllib.request, urllib.parse, urllib.error
import json
# Note that Google is increasingly requiring keys # for this API
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    url = serviceurl + urllib.parse.urlencode( {'address': address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    try:
        js =json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
         print(' = = = = Failure To Retrieve = = = =')
         print(data)
         continue
    print(json.dumps( js, indent = 4))
    lat = js["results"][ 0]["geometry"]["location"]["lat"]
    lng = js["results"][ 0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print( location)
