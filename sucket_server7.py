#!/usr/bin/python3
import sys, os
import socket
# import time
from mymodle import ServerObject

SO = ServerObject()

adr = SO.HOST, SO.PORT

YES = ['y', 'yes', 'yeah']
NO = ['n', 'no']

DATA = []
USERS  = []
SO.HOST = SO.GetPIp()
count = 0

def GetName(ip, USERS):
    if len(USERS) > 0:
        if any(ip in sublist[0] for sublist in USERS):
            for i in USERS:
                if ip == i[0]:
                    return i[1]
        else:
            return ip
    else:
        return ip


print(f"(+) ------ Any one can connect trough ip: {SO.HOST} ----- (+)")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(adr)

while True:
    s.listen(100)
    server, client = s.accept()
    with server:
        mode = server.recv(4)
        mode = mode.decode('utf-8')
        usename_ = SO.GetUseName(server, client[0])
        """
        if len(USERS) > 0:
            if any(client[0] in sublist[0] for sublist in USERS):
                pass
            else:
                USERS += usename_
        else:
            USERS += usename_
            """

        # +++++++print(f"\n\n{mode}")
        if mode == '_f__':
            print(f'(+) Initiating file transfer from {usename_[1]}........')
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
           # print(f"Connected to {usename_[1]} on port {client[1]}......")
            #+++++++print(f"User {usename_[1]} has connected......")
            if len(USERS) > 0:
                #if any(client[0] in sublist[0] for sublist in USERS) and (client[1] in [sublist[1] for sublist in USERS]):
                if (client[0] in [sublist[0] for sublist in USERS]) and (usename_[1] in [sublist[1] for sublist in USERS]):
                    for i in USERS:
                        if i[0] == client[0] and i[1] == usename_[1]:
                            index = i[2]
                else:
                    index = 1
            else:
                index = 1
            # DATA represent the total msg data
            # while HDATA represent only the unrecived data of a particular user
            HDATA = DATA[index - 1:]
            #print(HDATA)
            #print(DATA)
            #print(client[0], 'or', usename_[0])
            SO.SendOldMsg(server, HDATA)
            #to know if a client sent anything
            sent = server.recv(1)
            sent = sent.decode('utf-8')
            if sent == 't':
                data = server.recv(1024)
                ddata = data.decode('utf-8')
            else:
                data = ''
            if data:

                if ddata == "exit":
                    print(f"User {usename_[1]} has left")

                    if len(USERS) > 0:
                        if (client[0] in [sublist[0] for sublist in USERS]) and (usename_[1] in [sublist[1] for sublist in USERS]):
                            for i in USERS:
                                if i[0] == client[0] and i[1] == usename_[1]:
                                    i[2] = 1
                        else:
                            new = usename_ + [1]
                            USERS += [new]
                    else:
                        new = usename_ + [1]
                        USERS += [new]


                elif ddata == "exitall":
                    print("bye every one")
                    break


                else:
                    print(ddata)
                    # for stored message handling
                    count += 1
                    DATA += [[client[0], usename_[1], ddata, count]]

                    if len(USERS) > 0:
                        #if any(client[0] in sublist[0] for sublist in USERS) and (client[1] in [sublist[1] for sublist in USERS]):
                        if (client[0] in [sublist[0] for sublist in USERS]) and (usename_[1] in [sublist[1] for sublist in USERS]):
                            for i in USERS:
                                if i[0] == client[0] and i[1] == usename_[1]:
                                    i[2] = len(DATA)
                        else:
                            new = usename_ + [len(DATA)]
                            USERS += [new]
                    else:
                        new = usename_ + [len(DATA)]
                        USERS += [new]
print("..............")
s.close()
