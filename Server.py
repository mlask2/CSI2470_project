import socket
import threading

# server config
host = '127.0.0.1'
port = 55555
PASSWORD = "password"  # change password here
MAX_CLIENTS = 5           # change max clients allowed here 

# starts server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

# broadcasts to all clients
def broadcast(message):
    for client in clients:
        client.send(message)

# disconnects clients  
def remove_client(client):
    if client in clients:
        index = clients.index(client)
        nickname = nicknames[index]
        clients.remove(client)
        nicknames.remove(nickname)
        broadcast(f"{nickname} has left the chat.".encode('ascii'))
        client.close()

# handle communication
def handle(client):
    while True:
        try:
            # Receive and broadcast messages
            message = client.recv(1024)
            broadcast(message)
        except:
            remove_client(client)
            break

# accept and manage new clients
def receive():
    print("Server is running and listening...")
    while True:
        # accept a new connection here
        client, address = server.accept()
        
        # check if the max client limit is reached here
        if len(clients) >= MAX_CLIENTS:
            client.send('Server is full. Try again later.'.encode('ascii'))
            client.close()
            continue

        print(f"Connected with {str(address)}")

        # request password from the client
        client.send('PASS'.encode('ascii'))
        password = client.recv(1024).decode('ascii')
        if password != PASSWORD:
            client.send('Incorrect password. Disconnecting.'.encode('ascii'))
            client.close()
            continue

        # request and store nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))

        # start a thread to handle the client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
