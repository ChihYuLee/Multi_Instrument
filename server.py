import socket
import threading
import pickle

HEADER= 64
FORMAT='utf-8'
DISCONNECT_MESSAGE='!DISCONNECT'
PORT = 5050
SERVER =socket.gethostbyname(socket.gethostname())
#SERVER = '10.104.230.235'
ADDR= (SERVER, PORT)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
threads=[]


#String 
def handle_client(conn, addr):
    print('[NEW COONECTION] {} connected'.format(addr))
    connected =True
    while connected:
        ### String 
        msg_length= conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length= int(msg_length)
            msg= conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected= False
            print("{} {}".format(addr,msg))
            conn.send('Message received'.encode(FORMAT))

        ### Pickle
        data = conn.recv(4096)
        data_variable = pickle.loads(data)
    conn.close()

def start():
    server.listen()
    print('[LISTENING] Server is listening on {}'.format(SERVER))
    while True:
        conn, addr= server.accept()
        thread= threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print('[ACTIVE CONNECTIONS] {}'.format(threading.activeCount()-1))


print('[STARTING] Server is starting...')
start()