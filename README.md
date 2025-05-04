Chat App Using Socket Programming in Python
Welcome to the Python Chat Application! This project enables real-time communication between multiple clients using socket programming. With a user-friendly GUI built with Tkinter, you can seamlessly chat with others over a network.

Features:
Multi-client support – Connect multiple users simultaneously.
Real-time messaging – Instant chat with other connected clients.
User-friendly GUI – A simple yet intuitive Tkinter interface.
Unique username assignment – Join the chat with a personalized username.
Disconnect feature – Type !disconnect to exit the chat gracefully.

Prerequisites:Ensure you have the following installed before running the application:
Python 3.x

tkinter (Pre-installed with Python)

cd chat-app-socket-python
How to Run:
Start the Server
Run the following command to start the chat server:
python server.py
The server will listen for client connections on 127.0.0.1:8000.

Start a Client:
Run the client application in a separate terminal:
python client.py
Enter your username and click "Connect" to join the chat!
How It Works
Server Side (server.py)
Initializes a socket object and binds it to a host and port.
Accepts incoming connections and assigns threads to each client.
Receives and broadcasts messages to all connected clients.
Client Side (client.py)
Connects to the server using a socket.
Provides a Tkinter GUI for users to send and receive messages.
Displays incoming messages in a scrollable chat window.
Allows users to disconnect from the chat using !disconnect.

Project Files:
server.py – Server-side code for handling connections & broadcasting messages.client.py – Client-side code with a GUI for chat interaction.README.md – Comprehensive guide and instructions for using the app.

Example Usage:
Start the Server
python server.py
The server is now waiting for client connections.
Start a Client
python client.py
Enter a unique username and start chatting!
Send Messages
Type a message and press Enter to send it to all connected users.

Disconnect
Simply type !disconnect to leave the chat.


