#!/usr/bin/python3

import socket

# HOST = socket.gethostbyname(socket.gethostname())
HOST = ''
PORT = 9999
adr = HOST, PORT
mode = '_ms_'
print(HOST)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(adr)

while True:
    s.listen()
    server, client = s.accept()
    mode = server.recv(3)
    mode = mode.decode('utf-8')
    print(mode)
    if mode == '_f-':
        print('(+) Initiating file transfer........')
        msg = s.recive(1024)
        msg = msg.decode('utf-8')
        ans = input(f"{msg}:")
        s.sendall(b'ans')
        if ans.lower() == 'no':
            mode = '_ms_'
            continue
        else:
            size = s.recv(1024)
            size = int(size.decode('utf-8'))
            fname = s.recv(1024)
            fname = fname.decode('utf-8')
            with open(fname, 'wb') as bf:
                while size > 0:
                    data = s.recv(1024)
                    bf.write(data)
                    size -= len(data)
            print('!Done......')



    else:
        with server:
            print(f"Connected to {client[0]} on port {client[1]}......")
            data = server.recv(1024)
            ddata = data.decode('utf-8')
            if data:
                if ddata == "exit":
                    print(f"{client} has left")
                elif ddata == "exitall":
                    print("bye every one")
                    break
                else:
                    print(ddata)
print("..............")
s.close()
"""
while True:
    data = server.recv(1024)
    if not data:
        break
data = server.recv(1024)
server.sendall(data)
"""
