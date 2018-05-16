import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('202.120.108.14', 80))
mysock.send('GET http://202.120.108.14/ecustedu/K_StudentQuery/K_Default.aspx HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data;

mysock.close()
