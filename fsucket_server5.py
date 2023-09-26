#!/usr/bin/python3

import socket
import time
import mysocket

"""
   ---- UPDATE ------
* imported a costomised mode to make the sending and reciveing more solid

"""
# HOST = socket.gethostbyname(socket.gethostname())
HOST = ''
PORT = 9999
adr = HOST, PORT
mode = '_ms_'
print(HOST)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(adr)

while True:
    s.listen(100)
    server, client = s.accept()
    with server:
        mode = server.recv(4)
        mode = mode.decode('utf-8')
        print(mode)
        if mode == '_f__':
            print('(+) Initiating file transfer........')
            msg = server.recv(70)
            msg = msg.decode('utf-8')
            ans = input(f"{msg}:")
            ans += '\n'
            ans = ans.encode('utf-8')
            server.sendall(ans)
            if ans.lower() == 'no':
                mode = '_ms_'
                continue
            else:
                size = server.recv(1024)
                nsize = size.decode('utf-8')
                print(nsize)
                size = int(nsize)
                time.sleep(6)
                fname = server.recv(1024)
                server.sendall(b'\n')
                fname = fname.decode('utf-8')
                time.sleep(6)
                with open(fname, 'wb') as bf:
                    while size > 0:

                        data = server.recv(1024)
                        bf.write(data)
                        size -= len(data)
                print('!Done......')

        if mode != '_f__':
            print(f"Connected to {client[0]} on port {client[1]}......")
            data = server.recv(1024)
            print('vam')
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
