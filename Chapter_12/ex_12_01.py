#1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page.
#You can use split('/') to break the URL into its component parts so you can extract the host name for
#the socket connect call. Add error checking using try and except to handle the condition where
#the user enters an improperly formatted or non-existent URL.
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Enter : http://data.pr4e.org/romeo.txt')
url = input('Enter - url: ')
url_segments = url.split('/')
connect_segment = url_segments[2]
print ('url',url)
print ('connect_segment',connect_segment)
#mysock.connect(('data.pr4e.org', 80))
try:
    mysock.connect((connect_segment, 80))
except:
    print('Bad url input')
    quit()
#cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
get_request = 'Get '+str(url)+' HTTP/1.0\r\n\r\n'
print (get_request)
#quit()
#hey, this totally works
cmd = get_request.encode()
mysock.send(cmd)

#
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
