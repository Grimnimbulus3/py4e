# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
url = 'http://py4e-data.dr-chuck.net/known_by_Darius.html'
#moved the following two down in the sequence
#html = urllib.request.urlopen(url, context=ctx).read()
#soup = BeautifulSoup(html, 'html.parser')

#print (soup)
#modify to grab the third link and follow it, repeating 4 times
count = input('Enter count ')
count_int = int(count)
position = input('Enter position ')
position_int = int(position)
position_follow = position_int-1
#moved the numlist into the loop, hoping it will repopulate every time
#numlist = list()

#starts at this url, then updates at the end of the loop

count_iter = 0
while count_iter<=count_int:
    print ('Retrieving: '+ url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    numlist = list()
# Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        #print(tag.get('href', None))
        link = tag.get('href', None)
        numlist.append(link)
    link_follow = numlist[position_follow]
    #print (link_follow)
    url = link_follow
    count_iter=count_iter+1
