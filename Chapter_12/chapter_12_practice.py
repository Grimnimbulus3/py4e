#12.1
#12.2
#12.3
#12.4 Retrieving Web page_lines
#using urllib to retrieve web page_lines

# opens up and prints romeo.txt from data.pr4e.org
import urllib.request
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
     print( line.decode(). strip())

#opens up romeo.txt, counts through words using a dictioanry
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
     words = line.decode(). split()
     for word in words:
          counts[word] = counts.get(word, 0) + 1
print(counts)

#
# Search for lines that start with From and have an at sign
import urllib.request, urllib.parse, urllib.error

import re
print('Enter: http://www.dr-chuck.com/page1.htm')
url = input('Enter - ')
html = urllib.request.urlopen(url).read()
links = re.findall(b'href ="(http://.*?)"', html)
for link in links:
     print(link.decode())

#12.5 Parsing Web pages

# To run this, you can install BeautifulSoup #https://pypi.python.org/pypi/beautifulsoup4
# Or download the file # http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('Enter this: http://www.py4e.com/book.htm')
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

##
#Reading binary files using urllib
#http://www.py4e.com/code3/curl1.py
#reads the iamge into img variable, opens a local file(cover3.jpg) and writes the image into it
import urllib.request, urllib.parse, urllib.error
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand = open('cover3.jpg','wb')
fhand.write(img)
fhand.close()

#http://www.py4e.com/code3/curl2.py
# this does the same as http://www.py4e.com/code3/curl1.py, but puts in a buffer of 100,00 char at a time
import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied.')
fhand.close()
