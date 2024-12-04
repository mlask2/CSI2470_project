import socket
import threading

nickname = input("Pick a nickname: ")

# connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

# send password
password = input("Enter server password: ")
client.send(password.encode('ascii'))

# check for server response password
response = client.recv(1024).decode('ascii')
if response == 'Incorrect password. Disconnecting.':
    print(response)
    client.close()
    exit()

# receive 
def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except Exception as e:
            print(f"An error has occurred: {e}")
            client.close()
            break

# write
def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

# Start threads for receiving and writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
