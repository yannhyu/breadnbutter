# step_4_echoserver_via_coroutine.py
"""
(dabeaz) yann.yu@mllxv-yu:breadnbutter$ python coroutines/step_4_echoserver_via_coroutine.py 
Connection from ('127.0.0.1', 41144)
Connection from ('127.0.0.1', 41146)

can handle concurrency, and very large number of it
"""

from socket import *
import asyncio

async def echo_server(address, loop):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    sock.setblocking(False)
    while True:
        client, addr = await loop.sock_accept(sock)
        print('Connection from', addr)
        loop.create_task(echo_handler(client, loop))

async def echo_handler(client, loop):
    while True:
        data = await loop.sock_recv(client, 100000)
        if not data:
            break
        await loop.sock_sendall(client, b'Got:' + data)
    print('Connection closed')
    client.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(echo_server(('', 25000), loop))


