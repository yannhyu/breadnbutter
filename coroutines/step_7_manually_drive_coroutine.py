# step_7_manually_drive_coroutine.py
"""
(dabeaz) yann.yu@mllxv-yu:breadnbutter$ python coroutines/step_7_manually_drive_coroutine.py 
<__main__.Loop object at 0x7f2d3fb75ba8>
('recv', 'somesocket', 100000)
('sendall', 'somesocket', b'Got:What it is')
('recv', 'somesocket', 100000)
('sendall', 'somesocket', b'Got:How about')

request/response loop going on, running entirely
under the management of other code; yield is used
to suspend that code and make requests back to the event
loop.

low level details

"""
import types

class Loop(object):
    @types.coroutine
    def sock_recv(self, sock, maxsize):
        result = yield ('recv', sock, maxsize)
        return result

    @types.coroutine
    def sock_sendall(self, sock, data):
        result = yield ('sendall', sock, data)
        return result

if __name__ == '__main__':
    from step_4_echoserver_via_coroutine import echo_handler
    loop = Loop()
    print(loop)
    coro = echo_handler('somesocket', loop)
    print(coro.send(None))    # Wake up the generator
    print(coro.send(b'What it is'))    # Advance to the next await
    print(coro.send(None))
    print(coro.send(b'How about'))