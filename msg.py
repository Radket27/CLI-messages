import socket, time
from threading import *

def ser(msg,port,has):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ip = 'localhost'
    server.bind((ip, port))
    server.listen()
    odbiorca, nie = server.accept()
    print("connect with %s"%str(nie))
    if (has != True):
        odbiorca.sendall(bytes(msg,'utf8'))
        has = False
        odbiorca.close()
    return 0

def cli(ip,port):
    odbiorca = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    odbiorca.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    odbiorca.connect((ip,port))
    msg = odbiorca.recv(1024)
    msg = msg.decode()
    user, msg2 = decode2(msg)
    print('['+str(time.asctime())+'] '+str(user)+': '+str(msg2))
    odbiorca.close()
    return 0

def connect(user,msg):
    com = user + ';' + msg
    return com

def decode2(msg):
    user, text = msg.split(';',maxsplit=1)
    return user,text


if(__name__ == "__main__"):
    username = str(input("Name: "))
    ip = input("Server IP: ")
    port = int(input("Server port: "))
    why = input("Receive a message?(t/n): ")
    has = False
    if(why == 't'):
        has = True
    
    
    while True:
        if(has != True):
            msg = str(input("Message:\n"))
            text = connect(username,msg)
            li1 = Thread(target=ser, args=(text,port,has,))        
        li2 = Thread(target=cli, args=(ip,port,))
        if(has != True):
            li1.start()
        li2.start()



