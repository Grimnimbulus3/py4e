#Exercise 2: Change your socket program so that it counts the number of characters it has received
#and stops displaying any text after it has shown 3000 characters.
#The program should retrieve the entire document and count the total number of characters
#and display the count of the number of characters at the end of the document.
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
count = 0
while count<3000:
    data = mysock.recv(500)
    dat_len = len(data)
    if dat_len < 1:
        break
    else:
        count = count+dat_len
    print(data.decode(),end='')
print ('Characters:', count)

mysock.close()
