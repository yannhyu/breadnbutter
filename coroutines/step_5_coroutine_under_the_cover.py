# step_5_coroutine_under_the_cover.py

async def greeting(name):
    return 'hey, ' + name

if __name__ == '__main__':
    g = greeting('Under the cover')
    print(g)
    try:
        g.send(None)
    except StopIteration as si:
        result = si.value

    print(result)