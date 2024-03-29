import socket
from time import asctime
from threading import Thread

def ser(msg,port,has):
    """
    send message 
    (message,port,first_message #True or False)
    """
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
    """
    Recive and decode message
    (ip_another_computer,port_another_computer)
    """
    odbiorca = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    odbiorca.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    odbiorca.connect((ip,port))
    msg = odbiorca.recv(1024)
    msg = msg.decode()
    user, msg2 = decode2(msg)
    print('['+str(asctime())+'] '+str(user)+': '+str(msg2))
    odbiorca.close()
    return 0

def connect(user,msg):
    """
    prepare message to send
    (user_name,message)
    return merged message, ready to send
    """
    com = user + ';' + msg
    return com

def decode2(msg):
    """
    decode received message
    (message)
    return decoded message (user,message)
    """
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



