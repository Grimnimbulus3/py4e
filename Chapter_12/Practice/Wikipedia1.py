#try to connect to wikipedia and grab the text off a webpage
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('en.wikipedia.org', 80))
cmd = 'GET https://en.wikipedia.org/wiki/16-bit\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
