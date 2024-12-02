import socket
import threading

nickname = input("Pick a nickname: ")

# Defining a socket and connecting it to the server
client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.comment(('127.0.0.1', 55555))

# Defining the recieve function
def recieve():
    while True:
        try:
            message = client.recv(1024).decode('ascii') # Recieving messages from the server
            if message == 'NICK' :
                client.send(nickname.endcode('ascii'))
            else:
                print(message)
        except:  
            print("An error has occurred")
            client.close()
            break

# Defining the write function
def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
