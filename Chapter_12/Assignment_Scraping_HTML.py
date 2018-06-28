# the following is sample data

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
print(url)
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
numlist = list()
spans = soup('span')
for span in spans:
    words = span.decode()
    stuff = re.findall('([0-9]+)',words)
    if len(stuff) == 0 : continue
    for things in stuff:
        num = float(things)
        numlist.append(num)
print(numlist)
numlist_sum = sum(numlist)
print(numlist_sum)

    #comments = re.findall('"comments">([0-9]+)<', span)
    #print(comments)


#for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
