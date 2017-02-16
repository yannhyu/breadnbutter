# step_1_coroutine_overview.py

# a piece of code that is sitting there ready
# for some other manager type of program to run
async def greeting(name):
    return 'hey, ' + name

if __name__ == '__main__':
    g = greeting('coroutine')
    print(g)
    import asyncio
    loop = asyncio.get_event_loop()
    # running under management
    res = loop.run_until_complete(g)
    print(res)