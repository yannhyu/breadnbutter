# merge_nested_dicts.py

# tested under Python3.6
# assuming dict_02 overwrites dict_01
# one liner functional style
def deep_merge(dict_01, dict_02):
    return {k: {**dict_01.get(k), **dict_02.get(k)} if k in dict_01 and
                isinstance(dict_01.get(k), dict) and
                isinstance(dict_02.get(k), dict) else v 
                for k, v in {**dict_01, **dict_02}.items()}              

if __name__ == '__main__':
    y = {2: {'a': 1, 'b': 1}, 1: {'a': 1, 'b': 1}}
    x = {3: {'a': 1}, 2: {'a': 2, 'c': 2}}

    print(x)
    print(y)
    print(deep_merge(x, y))

'''
{3: {'a': 1}, 2: {'a': 2, 'c': 2}}
{2: {'a': 1, 'b': 1}, 1: {'a': 1, 'b': 1}}
{3: {'a': 1}, 2: {'a': 1, 'c': 2, 'b': 1}, 1: {'a': 1, 'b': 1}}
'''
