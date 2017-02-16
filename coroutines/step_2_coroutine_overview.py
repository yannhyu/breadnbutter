# step_2_await.py

# function running under management
async def greeting(name):
    return 'hey, ' + name

async def hello():
    names = ['Ross', 'Frank', 'Bennet']
    for name in names:
        print(await greeting(name))

if __name__ == '__main__':
    h = hello()
    print(h)
    import asyncio
    loop = asyncio.get_event_loop()
    # running under management
    loop.run_until_complete(h)