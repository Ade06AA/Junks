#!/usr/bin/python3
import sys, os
import socket
# import time
from mymodle import ServerObject

SO = ServerObject()

adr = SO.HOST, SO.PORT

YES = ['y', 'yes', 'yeah']
NO = ['n', 'no']


SO.HOST = SO.GetPIp()


print(f"(+) ------ Any one can connect trough ip: {SO.HOST} ----- (+)")
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
            #1  nm = server.recv(5)
            # 1 nm = int(nm.decode('utf-8'))
            #1  msg = server.recv(nm)
            msg = SO.MyMsgRecv(server) #1
            """
            msg = b''
            while True:
                print(1)
                nf = s.recv(1024)
                if not nf:
                    break
                msg += nf
                if b'\n' in nf:
                    break
            """
            #1  msg = msg.decode('utf-8')
            ans = input(f"{msg}:")
            #2   ans += '\n'
            #2   ans = ans.encode('utf-8')
            #2   server.sendall(ans)
            SO.MyMsgSend(server, ans) #2
            if ans.lower() in NO:
                mode = '_ms_'
                continue
            else:
                size = SO.MyMsgRecv(server) #3
                #3 size = server.recv(1024)
                #3 nsize = size.decode('utf-8')
                print(size)
                size = int(size)
                #3 time.sleep(6)
                #4 fname = server.recv(1024)
                fname = SO.MyMsgRecv(server)
                #4 server.sendall(b'\n')
                file = os.path.abspath(fname)
                if os.path.isfile(file):
                    print('This file is alredy present in this folder do you want to replace it?', end=' ')
                    out = input()
                else:
                    out = 'y'
                if out not in YES:
                    print(" (+) Terminating file transfer.....")
                    server.sendall(b'n')
                    continue
                else:
                    server.sendall(b'y')
                #5 time.sleep(6)
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
