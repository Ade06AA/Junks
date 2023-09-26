#!/usr/bin/python3

import os, socket, sys, time
"""  ******************************
relies on HOST sys.argv
******************************
"""

class ClientObject:
    """
    this class contains all the nessesry fuinction neede for a flexible 
    message transfer. the reason for using a class is to avoid multiple inportation of the neede libraries. all the is needed is to just create an object of this class which automatically import the neede libraries
    """
    def __init__(self):
        """
        seting up the nesesities
        """
        # importing the neede libraries
        import os, socket, sys, time, re
        # unrecived message
        self.MSG = []
        # total message history
        self.TMSG = []
        self.hostname = socket.gethostname()
        self.HOST = socket.gethostbyname(self.hostname)
        self.PORT = 9990
        self.YES = ['yes', 'yeah', 'y']
        self.NO = ['n', 'nah', 'no']
        # the arguments passed when runing the script
        self.arg = sys.argv
        # a flage flag that determines if the connection is in message mode or file transfer mode
        self.flag = '_ms_'
        # this is a pertern matching for ip address
        self.patern = re.compile(r'((\d{3}|\d{2}|\d{1})\.){3}(\d{3}|\d{2}|\d{1})')
    
    def RecvOldMsg(self, soc):
        """
        it recive unread messages from the server
        """
        self.MSG = []
        msg = soc.recv(1024)
        msg = msg.decode('utf-8')
        if msg == '_e_':
            soc.sendall(b'_c_')
            return
        while msg != '_d_':
            self.MSG += [eval(msg)]
            soc.sendall(b'_c_')
            msg = soc.recv(1024)
            msg = msg.decode('utf-8')
        self.TMSG += self.MSG
        if len(self.MSG) != 0:
            #print(self.MSG)
            #print(self.TMSG)
            for m in self.MSG:
                # print('run', m[1], '--', m[0], '==', self.HOST, '(', m[2])
                if (m[0] != self.HOST or m[1] != self.hostname) and m[0] != '127.0.0.1':
                    print("\n\n('_'){{({}) - ({})}} \n......: {}".format(m[0], m[1], m[2]))


    def SendUseName(self, soc):
        """
        send the name of the user
        """
        l = len(self.hostname)
        l = "{:0>8}".format(l)
        soc.sendall(l.encode('utf-8'))
        soc.recv(1)
        name = self.hostname
        soc.sendall(name.encode('utf-8'))


    def MyMsgSend(self, soc, msg):
        """
        impliment someting like a three hand shake
        while sending using sockets send func
        """
        l = len(msg)
        l = "{:0>8}".format(l)
        soc.sendall(l.encode('utf-8'))
        soc.recv(1)
        soc.sendall(msg.encode('utf-8'))



    def MyMsgRecv(self, soc):
        """
        impliment someting like a three hand shake
        while sending using sockets send func
        """
        n = soc.recv(8)
        n = n.decode('utf-8')
        soc.send(b'.')
        msg = soc.recv(int(n))
        return msg.decode('utf-8')

    def usage(self):
        """
        print out the script usage
        """
        print("(+) ussage:")
        print("""
            (+) python3 sucket_client5.py
            (+) python3 sucket_client5.py <flag>
            (+) python3 sucket_client5.py <flag> <server ip>
            (+) python3 sucket_client5.py <server ip>
            where flag == -f
            """)

    def arg_check(self):
        """
        chect the arguments passed when runing the script and do the needed
        """
        if len(self.arg) == 1:
            print('(++) Do you intend to pass an argument befor runing the script', end='')
            ans = input(': ')
            if ans in self.YES:
                narg = input('(++) input the argument ->: ')
                self.arg += narg.split()
        if len(self.arg) == 2:
            if self.arg[1]  == "-f":
                while True:
                    Y_N = input("(++) Do you want to send a file: ")
                    if Y_N.lower() in self.YES:
                        self.flag = "_f__"
                        break
                    if Y_N.lower() in self.NO:
                        aa = input("(++) Then do you want to chat ?: ")
                        if aa.lower() in self.YES:
                            self.flag = "_ms_"
                            break
                        else:
                            sys.exit()
            elif self.patern.fullmatch(self.arg[1]):
                print("(+) setting host")
                self.HOST = self.arg[1]
                print(self.HOST)
            else:
                self.usage()

        elif len(self.arg) == 3:
            if self.arg[1]  == "-f" and self.patern.fullmatch(self.arg[2]):
                HOST = self.arg[2]
                while True:
                    Y_N = input("(++) Do you want to send a file: ")
                    if Y_N.lower() in self.YES:
                        self.flag = "_f__"
                        break
                    if Y_N.lower() in self.NO:
                        aa = input("Then do you want to chat ?: ")
                        if aa.lower() in self.YES:
                            self.flag = "_ms_"
                            break
                        else:
                            sys.exit()
            else:
                self.usage()
                self.arg = self.arg[:1]
                self.arg_check()
        elif len(self.arg) > 3:
            self.usage()
            self.arg = self.arg[:1]
            self.arg_check()


class ServerObject:
    """
    this is a class for an object that mannages the server functions
    """

    def __init__(self):
        """
        seting up the nesesities
        """
        # importing the neede libraries
        import os, socket, sys, time, re
        hostname = socket.gethostname()
        self.HOST = ''
        self.host = socket.gethostbyname(hostname)
        self.PORT = 9990
        self.YES = ['yes', 'yeah', 'y']
        self.NO = ['n', 'nah', 'no']
        # the arguments passed when runing the script
        self.arg = sys.argv
        # a flage flag that determines if the connection is in message mode or file transfer mode
        self.flag = '_ms_'
        # this is a pertern matching for ip address
        self.patern = re.compile(r'((\d{3}|\d{2}|\d{1})\.){3}(\d{3}|\d{2}|\d{1})')

    def SendOldMsg(self, soc, DATA):
        """
        send unrecived message to client
        """
        # print('++++++', DATA)
        if len(DATA) == 0:
            soc.sendall(b'_e_')
            soc.recv(3)
        else:
            for d in DATA:
                msg = str(d).encode('utf-8')
                soc.sendall(msg)
                soc.recv(3)
            soc.sendall(b'_d_')


    def GetUseName(self, soc, ip):
        """
        get the name of the user
        """
        n = soc.recv(8)
        n = n.decode('utf-8')
        soc.send(b'.')
        name = soc.recv(int(n))
        name = name.decode('utf-8')
        return [ip, name]


    def MyMsgSend(self, soc, msg):
        """
        impliment someting like a three hand shake
        while sending using sockets send func
        """
        l = len(msg)
        l = "{:0>8}".format(l)
        soc.sendall(l.encode('utf-8'))
        soc.recv(1)
        soc.sendall(msg.encode('utf-8'))



    def MyMsgRecv(self, soc):
        """
        impliment someting like a three hand shake
        while sending using sockets send func
        """
        n = soc.recv(8)
        n = n.decode('utf-8')
        soc.send(b'.')
        msg = soc.recv(int(n))
        return msg.decode('utf-8')

    def GetPIp(self):
        """
        this func tries to get the public ip of the server
        else returns the the local ip
        """
        try:
            try:
                requests = __import__('requests')
            except:
                print('(+) you dont have python requests library')
                print("""
                (+)  you can try geting this systems ip manually
                ...  by using ipconfig or try using google: type "my ip address"
                ...  on google then any client can connect to this server using that
                ...  ip if you are connected to the internet
                      """)
                raise
            responce = request.get("https://httpsbin.org/ip")
            data = responce.json()
            print('request is working as expected ...........')
            ip = data.get['origin']
            return ip
        except Exception:
            print("""
            (+) there was an error
            (+) pls make sure u are connected to the internet
            (+) if you intend to use local connection enter y: """, end=' ')
            ans = input()
            if ans in self.YES:
                return self.host
            sys.exit()

