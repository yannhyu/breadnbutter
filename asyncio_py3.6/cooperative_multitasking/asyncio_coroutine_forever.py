# asyncio_coroutine_forever.py

import asyncio

async def hello_world():
    await asyncio.sleep(1)
    print('Hello World')
    await good_evening()

async def good_evening():
    await asyncio.sleep(1)
    print('Good Evening')
    await hello_world()

loop = asyncio.get_event_loop()
try:

    loop.run_until_complete(hello_world())
    loop.run_until_complete(good_evening())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print('closing event loop')
    loop.close()