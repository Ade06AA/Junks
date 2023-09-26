#!/usr/bin/python3
import sys, os
import socket
import time

HOST = ''
PORT = 9999
adr = HOST, PORT
mode = '_ms_'
hostname = socket.gethostname()     # get the name of the user
host = socket.gethostbyname(hostname)   # get the local ip addrerss of the user
YES = ['y', 'yes', 'yeah']
NO = ['n', 'no']
def GetPIp():
    """
    this fun tries to get the public ip of the server
    else returns the the local ip
    """
    try:
        try:
            requests = __import__('requests')
        except:
            print(' (+)  you dont have python requests library')
            print(""" (+)  you can try geting your this systems ip manually
                  by using ipconfig or google: type "my ip" on google
                  then any one can connect to this server using that
                  ip is you are connected to the internet""")
            raise
        responce = request.get("https://httpsbin.org/ip")
        data = responce.json()
        ip = data.get['origin']
        return ip
    except Exception:
        print("""
        (+) there was an error
        (+) pls make sure u are connected to the internet
        (+) if you intend to use local connection enter y:
        """, end=' ')
        ans = input()
        if ans in YES:
            return host
        return None

host = GetPIp()
if host is None:
    sys.exit()
print(f"(+) ------ Any one can connect trough ip: {host} ----- (+)")
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
            nm = server.recv(5)
            nm = int(nm.decode('utf-8'))
            msg = server.recv(nm)
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
            msg = msg.decode('utf-8')
            ans = input(f"{msg}:")
            ans += '\n'
            ans = ans.encode('utf-8')
            server.sendall(ans)
            if ans.lower() in NO:
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
