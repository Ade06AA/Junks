#!/usr/bin/python3

import socket
import sys
import os

HOST='192.168.75.128'
PORT = 9999
adr = HOST, PORT
flag = "_ms_"

if len(sys.argv) == 2:
    if sys.argv[1]  == "-f":
        while True:
            Y_N = input("Do you want to send a file: ")
            if Y_N.lower() == "yes":
                flag = "_f_"
                break
            if Y_N.lower() == "no":
                aa = input("Then do you want to chat ?: ")
                if aa.lower() == "yes":
                    flag = "_ms_"
                    break
                else:
                    sys.exit()
if flag == "_f_":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(adr)
        print("Enter the name of the file to be sent")
        print("example: myfile.txt")
        print("If the file is not in this curent folder input the file absolute path")
        File = input("(input) ->: ")
        file = os.path.abspath(File)
        if os.path.isfile(file):
            print('file present....')
            size = os.path.getsize(file)
            msg = f"This transfer is going to take {size}byte of your memory do u acsept it"
            
            s.sendall(b'_f_')
            s.sendall(msg.encode('utf-8'))
            f = s.recv(1024)
            f = f.decode("utf-8")
            if f.lower() == "no":
                sys.exit()
            with open(file, "rb") as nfile:
                # sends the size of the file
                size = str(size).encode('utf-8')
                s.sendall(size)
                s.sendall(os.path.basename(file).encode('utf-8'))
                data = nfile.read(1024)
                while data:
                    s.sendall(data)
                    data = nfile.read(1024)
            print('Done.........')





# HOST = socket.gethostbyname(socket.gethostname())
if flag == "_ms_":
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(adr)
            nn = ''
            s.sendall('_ms_')
            while nn.strip() == '':
                nn = input('..')
            dnn = nn.encode('utf-8')
            s.sendall(dnn)
        if nn == "exit" or nn == "exitall":
            break
#print(f"Recive {data.decode('utf-8')}")
