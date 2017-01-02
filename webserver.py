#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket

class webserver:
  HOST, PORT = '', 8888
  
  listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  listen_socket.bind((HOST, PORT))
  listen_socket.listen(1)
  print('Serving HTTP on port {0}'.format(PORT))
  while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print(request)
    
    http_response = b"""\
 HTTP/1.1 200 OK
 
 Hello, World!
 """
    client_connection.sendall(http_response)  
    client_connection.close()
    
if __name__=='__main__':
  webserver()