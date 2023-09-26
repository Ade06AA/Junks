#!/usr/bin/python3
import time
import socket
import sys
import os
import re


hostname = socket.gethostname()
HOST = socket.gethostbyname(hostname)
PORT = 9999
flag = "_ms_"
# pertern matching in order to identify an ip
patern = re.compile(r'((\d{3}|\d{2}|\d{1})\.){3}(\d{3}|\d{2}|\d{1})')
YES = ['y', 'yes', 'yeah']
NO = ['n', 'no', 'nah']
print("""  
    NOTE: By defualt this client connects to the local network if you intend to connect
    to a external network pls run the script again while specifying the ip of the sever,
    also make sure you are connected to the internet """)
if len(sys.argv) == 2:
    if sys.argv[1]  == "-f":
        while True:
            Y_N = input("Do you want to send a file: ")
            if Y_N.lower() in YES:
                flag = "_f__"
                break
            if Y_N.lower() in NO:
                aa = input("Then do you want to chat ?: ")
                if aa.lower() in YES:
                    flag = "_ms_"
                    break
                else:
                    sys.exit()
    elif patern.fullmatch(sys.argv[1]):
        print("(+) setting host")
        HOST = sys.argv[1]
        print(HOST)
    else:
        print("(+) ussage:")
        print("""
        python3 sucket_client4.py <flag>
        python3 sucket_client4.py <flag> <server ip>
        python3 sucket_client4.py <server ip>
        where flag == -f
        """)

elif len(sys.argv) == 3:
    if sys.argv[1]  == "-f" and patern.fullmatch(sys.argv[2]):
        HOST = sys.argv[2]
        while True:
            Y_N = input("Do you want to send a file: ")
            if Y_N.lower() in YES:
                flag = "_f__"
                break
            if Y_N.lower() in NO:
                aa = input("Then do you want to chat ?: ")
                if aa.lower() in YES:
                    flag = "_ms_"
                    break
                else:
                    sys.exit()
    else:
        print("(+) ussage:")
        print("""
        python3 sucket_client4.py <flag>
        python3 sucket_client4.py <flag> <server ip>
        python3 sucket_client4.py <server ip>
        where flag == -f
        """)

adr = HOST, PORT

if flag == "_f__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f'Trying to connect to {HOST}')
        s.connect(adr)
        print("Enter the name of the file to be sent")
        print("example: myfile.txt")
        print("If the file is not in this curent folder input the file absolute path")
        File = input("(input) ->: ")
        file = os.path.abspath(File)
        if os.path.isfile(file):
            print('file present....')
            size = os.path.getsize(file)
            rsize = size
            msg = f"This transfer is going to take {size}byte of your memory do u acsept it\n"
            
            lmsg = len(msg)
            s.sendall(b'_f__')
            lmsg = "{:0>5}".format(lmsg)
            s.sendall(lmsg.encode('utf-8'))
            s.sendall(msg.encode('utf-8'))
            newf = b''
            while True:
                f = s.recv(1024)
                if not f:
                    break
                newf += f
                if b'\n' in f:
                    break
            newf = newf.decode("utf-8")
            if newf.lower() == "no":
                sys.exit()
            with open(file, "rb") as nfile:
                # sends the size of the file
                # input("sending file size")
                size = str(size).encode('utf-8')
                time.sleep(6)
                s.sendall(size)
                # input("sending file name")
                time.sleep(6)
                s.sendall(os.path.basename(file).encode('utf-8'))
                s.recv(1)
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
if flag == "_ms_":
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print(f'Trying to connect to {HOST}')
            s.connect(adr)
            nn = ''
            s.sendall(b'_ms_')
            while nn.strip() == '':
                nn = input('..')
            dnn = nn.encode('utf-8')
            s.sendall(dnn)
        if nn == "exit" or nn == "exitall":
            break
#print(f"Recive {data.decode('utf-8')}")
