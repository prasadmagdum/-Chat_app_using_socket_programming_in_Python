
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import time

HOST = '127.0.0.1'
PORT = 8000
CLIENT_BUFFER = 6
CONNECTED = 1
INPUT_BUFFER = 2048
ADDR = (HOST,PORT)
ACTIVE_CLIENTS = []
FORMAT = 'utf-8'
root= tk.Tk()

def listen_for_message(client, client_name):
    while CONNECTED:
        msg = client.recv(INPUT_BUFFER).decode(FORMAT)
        if msg != '':
            if msg == '!disconnect':
                print(f'Disconnecting You From The Server')
                time.sleep(2)
                client.close()
                root.close()
            else:
                final_msg = client_name + '~'+ msg
                send_message_all(final_msg)
        else:
            print('The Message Is Empty')

def send_message_to_user(client, msg):
    client.sendall(msg.encode())

def send_message_all(msg):
    for user in ACTIVE_CLIENTS:
        send_message_to_user(user[1], msg)

def username_handler(client):
    
    while CONNECTED:
        client_name = client.recv(INPUT_BUFFER).decode(FORMAT)
        
        if client_name != '':
            ACTIVE_CLIENTS.append((client_name, client))
            prompt_message = "SERVER~" + f"{client_name} added to the chat"
            send_message_all(prompt_message)
            break
        else:
            print(f'Username Is Empty')
    
    threading.Thread(target=listen_for_message, args=(client,client_name, )).start()

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(ADDR)
        print(f'[SERVER CONNECTION] Server is Listening On {HOST} with Port {PORT}')
    except:
        print(f'[Connection Error]: Your Connection To Host: {HOST} with Port Number: {PORT} Failed')
    
    server.listen(CLIENT_BUFFER)

    while CONNECTED:
        client , address = server.accept()
        print(f"Successfully connected to client {address[0]} {address[1]}")
    
        threading.Thread(target=username_handler, args=(client, )).start()

 
if __name__ == '__main__':
    print(f'[SERVER STARTING] Server Is Starting...')
    main()
          