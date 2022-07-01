import socket
import threading
import pickle

HEADER= 64
FORMAT='utf-8'
DISCONNECT_MESSAGE='!DISCONNECT'
PORT = 5050
SERVER = '10.104.230.235'
ADDR= (SERVER, PORT)

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send_string(msg):
    message= msg.encode(FORMAT)
    msg_length =len(message)
    send_length= str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER-len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

def send_pickle(msg):
    data_string=pickle.dumps(msg)
    client.send(data_string)

send_string('Hello!')
send_string('JENG!')
send_string(DISCONNECT_MESSAGE)