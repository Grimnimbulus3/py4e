import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = input("Enter location: ")
print("retrieving ", url)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen(url, context=ctx).read()
#print (html)
root = ET.fromstring(html)
#print(root.tag)
#print (tree)
toplevel = root.findall(".")
#print("toplevel: ",toplevel)
children = root.findall("*")
#print(children)
comments = root.findall("./comments/comment")
#print('comments_children', comments)

#list = root.findall('commentinfo/comments/comment/user')
#print ('list :', list)

numlist = list()

for item in comments:
    #print('Name', item.find('name').text)
    #print(item.find('count').text)
    item_name = item.find('name').text
    item_count = item.find('count').text

    item_count_float = float(item_count)
    numlist.append(item_count_float)

count_sum = sum(numlist)
print(count_sum)
