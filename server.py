import argparse
import socket
import threading

FORMAT = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())
parser = argparse.ArgumentParser(description='The port you want your server to run')
parser.add_argument('PORT', type=int, help='Need the port for the server to run')
args = parser.parse_args()
ADDR = (SERVER, args.PORT)
DISCONNECT_msg = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def broadcast_re(msg, connections):
    for clientss in clients:
        if clientss != connections:
            try:
                clientss.send(msg)
            except:
                clientss.close()


def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast_re(message, client)
            print(message.decode('ascii'))
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break


def receive():
    server.listen()
    print("For help type: /help")
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


def suggestions():
    while True:
        message = input("You: ")
        if message == '/listall':
            print(nicknames, clients)
        elif message == '/ask':
            ask = input('Q: ')
            broadcast(f'[QUESTION] {ask}'.encode('ascii'))
        elif message == '/help':
            print(f'commands:\n/listall (lists all the active users and their connetion)\n/ask (Ask the bot a simple '
                  f'question)') 
        else:
            broadcast(f'[SERVER] {message}'.encode('ascii'))


thread_sugg = threading.Thread(target=suggestions)
thread_sugg.start()
receive()
