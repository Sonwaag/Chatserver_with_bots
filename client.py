import random
import socket
import argparse
import time

parser = argparse.ArgumentParser(description='Need the port and bot name')
parser.add_argument('PORT', type=int, help='The port of the server you want to connect to')
parser.add_argument('botname', type=str,
                    help='The bot you want to connect with. Availible BOTS: Helle, Daniel, Eirik and Ruben')
args = parser.parse_args()
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, args.PORT)

bot = args.botname
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def write():
    message = client.recv(1024).decode('ascii')
    if message == 'NICK':
        client.send(bot.encode('ascii'))
    if bot == "Bob":
        bob()
    elif bot == "Daniel":
        daniel()
    elif bot == "Helle":
        helle()
    elif bot == "Eirik":
        eirik()


def bob():
    while True:
        try:
            action = client.recv(1024).decode('ascii')
            print(action)
            if "[QUESTION]" in action:
                find_word = lastWord(action)
                response = bob_response(find_word)
                client.send('{}: {}'.format(bot, response).encode('ascii'))
            elif '[SERVER]' in action:
                respond = "You should try to ask us a question with the /ask command"
                client.send('{}: {}'.format(bot, respond).encode('ascii'))
        except:
            print('Somethin bad happend')
            break


def daniel():
    while True:
        try:
            action = client.recv(1024).decode('ascii')
            print(action)
            if "[QUESTION]" in action:
                find_word = lastWord(action)
                response = daniel_response(find_word)
                client.send('{}: {}'.format(bot, response).encode('ascii'))
            elif '[SERVER]' in action:
                respond = "You should try to ask us a question with the /ask command"
                client.send('{}: {}'.format(bot, respond).encode('ascii'))
        except:
            print('Somethin bad happend')
            break


def helle():
    while True:
        try:
            action = client.recv(1024).decode('ascii')
            print(action)
            if "[QUESTION]" in action:
                find_word = lastWord(action)
                response = helle_response(find_word)
                time.sleep(2)
                client.send('{}: {}'.format(bot, response).encode('ascii'))
            elif '[SERVER]' in action:
                respond = "You should try to ask us a question with the /ask command"
                client.send('{}: {}'.format(bot, respond).encode('ascii'))
        except:
            print('Somethin bad happend')
            break


def eirik():
    while True:
        try:
            action = client.recv(1024).decode('ascii')
            print(action)
            if "[QUESTION]" in action:
                find_word = lastWord(action)
                response = eirik_response(find_word)
                time.sleep(1)
                client.send('{}: {}'.format(bot, response).encode('ascii'))
            elif '[SERVER]' in action:
                respond = "You should try to ask us a question with the /ask command"
                client.send('{}: {}'.format(bot, respond).encode('ascii'))
        except:
            print('Somethin bad happend')
            break


def eirik_response(a):
    e_resp = 'Yesss lets go {} today!!'.format(a)
    return e_resp


def helle_response(a, b = None):
    alternatives = ['portfolio', 'eksams', 'party']
    b = random.choice(alternatives)
    e_resp = 'aghhh.. why do we have to {}, we just did the {}!!'.format(a, b)
    return e_resp


def bob_response(a, b = None):
    e_resp = 'Yesss lets go {} today!!'.format(a)
    return e_resp


def daniel_response(a):
    e_resp = 'Yesss lets go {} today!!'.format(a)
    return e_resp



def lastWord(string):
    # split by space and converting
    # string to list and
    lis = list(string.split(" "))

    # length of list
    length = len(lis)

    # returning last element in list
    response = lis[length - 1]
    return response.replace('?', '')


# receive_thread = threading.Thread(target=receive)
# receive_thread.start()

write()
