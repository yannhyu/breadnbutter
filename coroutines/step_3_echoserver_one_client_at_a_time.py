# step_3_echoserver_one_client_at_a_time.py
"""
(dabeaz) yann.yu@mllxv-yu:Data$ nc localhost 25000
hey
Got:hey
you
Got:you
how you doing slim?
Got:how you doing slim?

the limitation of this code: it can only handle one
client connection at a time... a second client is not
served until the first one closes its connection.
"""

from socket import *

def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        print('Connection from', addr)
        echo_handler(client)

def echo_handler(client):
    while True:
        data = client.recv(100000)
        if not data:
            break
        client.sendall(b'Got:' + data)
    print('Connection closed')
    client.close()


if __name__ == '__main__':
    echo_server(('', 25000))


