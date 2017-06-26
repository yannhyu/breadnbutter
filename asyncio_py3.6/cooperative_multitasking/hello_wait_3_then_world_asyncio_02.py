# hello_wait_3_then_world_asyncio_02.py

import asyncio

loop = asyncio.get_event_loop()

async def hello():
    print('Hello')
    await asyncio.sleep(3)
    print('World!')

if __name__ == '__main__':
    loop.run_until_complete(hello())    