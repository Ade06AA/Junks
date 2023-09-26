#!/usr/bin/python3
import time
import socket
import sys
import os
import re
from mymodle import ClientObject

CO = ClientObject()


# pertern matching in order to identify an ip
YES = ['y', 'yes', 'yeah']
NO = ['n', 'no', 'nah']
print("""  
    NOTE: By defualt this client connects to the local network if you intend to connect
    to a external network pls run the script again while specifying the ip of the sever,
    also make sure you are connected to the internet """)
CO.arg_check()

adr = CO.HOST, CO.PORT

if CO.flag == "_f__":
    print(CO.flag)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f'Trying to connect to {CO.HOST}')
        s.connect(adr)
        print("Enter the name of the file to be sent")
        print("example: myfile.txt")
        print("If the file is not in this curent folder input the file absolute path")
        File = input("(input) ->: ")
        file = os.path.abspath(File)
        # +++++ need to determin what happens if the file is not present
        if os.path.isfile(file):
            print('file present....')
            size = os.path.getsize(file)
            rsize = size
            msg = f"This transfer is going to take {size}byte of your memory do u acsept it"
            
            #1 lmsg = len(msg)
            s.sendall(b'_f__')
            CO.SendUseName(s)
            #1  lmsg = "{:0>5}".format(lmsg)
            #1  s.sendall(lmsg.encode('utf-8'))
            #1  s.sendall(msg.encode('utf-8'))
            CO.MyMsgSend(s, msg)
            #2  newf = b''
            #2  while True:
            #2      f = s.recv(1024)
            #2      if not f:
            #2          break
            #2      newf += f
            #2      if b'\n' in f:
            #2          break
            #2  newf = newf.decode("utf-8")
            newf = CO.MyMsgRecv(s)    #2
            if newf.lower() in NO:
                sys.exit()
            with open(file, "rb") as nfile:
                # sends the size of the file
                # input("sending file size")
                #3 size = str(size).encode('utf-8')
                #3 time.sleep(6)
                #3 s.sendall(size)
                CO.MyMsgSend(s, str(size))  #3
                # input("sending file name")
                #3 time.sleep(6)
                #4 s.sendall(os.path.basename(file).encode('utf-8'))
                CO.MyMsgSend(s, os.path.basename(file)) #4
                #4 s.recv(1)
                print('ooooooooo')
                ans = s.recv(1)
                print('ooooooooo')
                if ans.decode('utf-8') == 'n':
                    print("(+) File transfer has been treminated")
                    sys.exit()
                data = nfile.read(1024)
                while data:
                    s.sendall(data)
                    data = nfile.read(1024)
            print('Done.........')





# HOST = socket.gethostbyname(socket.gethostname())
if CO.flag == "_ms_":
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # *** print(f'Trying to connect to {CO.HOST}')
            s.connect(adr)
            nn = ''
            s.sendall(b'_ms_')
            CO.SendUseName(s)
            CO.RecvOldMsg(s)
            while nn.strip() == '':
                nn = input('\n\n:D {{(ME) - ({}) }}\n ........: '.format(CO.hostname))
            dnn = nn.encode('utf-8')
            s.sendall(dnn)
        if nn == "exit" or nn == "exitall":
            break
#print(f"Recive {data.decode('utf-8')}")
