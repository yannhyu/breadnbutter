# asyncio_coroutine_return.py

import asyncio

async def coroutine():
    print('inside coroutine')
    return 'coroutine result'


event_loop = asyncio.get_event_loop()
try:
    print('starting coroutine')
    coro = coroutine()
    print('entering event loop')
    res = event_loop.run_until_complete(coro)
    print('it returned: {!r}'.format(res))
finally:
    print('closing event loop')
    event_loop.close()