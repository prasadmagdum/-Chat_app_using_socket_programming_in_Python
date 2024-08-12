# -Chat_app_using_socket_programming_in_Python
A chat app using socket programming in Python enables real-time communication between clients over a network by establishing a connection through sockets.
Python Chat Application using Socket Programming
Overview
This repository contains a simple chat application built using socket programming in Python. The application allows multiple clients to connect to a server and communicate with each other in real-time. The client-side interface is built using the tkinter library to provide a graphical user interface (GUI) for ease of use.

Features
Multi-client support: The server can handle multiple clients simultaneously.
Real-time messaging: Clients can send and receive messages in real-time.
Graphical User Interface: The client has a simple GUI built with tkinter.
Username assignment: Each client must provide a unique username to join the chat.
Disconnect feature: Clients can disconnect from the chat using the !disconnect command.
Prerequisites
Before running the application, ensure you have the following installed:

Python 3.x
Basic knowledge of Python, socket programming, and tkinter
Installation
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/yourusername/chat-app-socket-python.git
Navigate to the project directory:

bash
Copy code
cd chat-app-socket-python
How to Run
Server
To start the server, run the following command in your terminal:

bash
Copy code
python server.py
The server will start and begin listening for incoming client connections on 127.0.0.1:8000.

Client
To start the client, run the following command in another terminal:

bash
Copy code
python client.py
The client window will open. Enter your desired username and click the "Connect" button.

Once connected, you can start chatting with other connected clients. Messages are displayed in the chat window, and you can send messages using the input box at the bottom.

How It Works
Server
The server script (server.py) initializes a socket object and binds it to a specified host and port.
It listens for incoming connections, accepts them, and assigns each client a separate thread for communication.
The server receives messages from clients, processes them, and broadcasts them to all connected clients.
Client
The client script (client.py) also initializes a socket object and connects to the server.
The client GUI allows users to enter their username, connect to the server, and send/receive messages.
Messages are displayed in the scrollable text area, and the input box is used for typing messages.
Clients can disconnect from the chat by typing !disconnect.
Files
server.py: Contains the server-side code for handling client connections and message broadcasting.
client.py: Contains the client-side code with a GUI for sending and receiving messages.
README.md: This file, providing an overview and instructions for the project.
Example Usage
Server: Start the server in one terminal:

bash
Copy code
python server.py
The server will start listening for clients.

Client: Start a client in another terminal:

bash
Copy code
python client.py
Enter a username in the GUI and start chatting.

Messaging: Clients can send messages that will be broadcasted to all connected users.

Disconnect: A client can disconnect by typing !disconnect.
