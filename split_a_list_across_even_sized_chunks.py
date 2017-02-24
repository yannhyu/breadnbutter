# split_a_list_across_even_sized_chunks.py

import pprint

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

pprint.pprint(list(chunks(range(10, 75), 10)))

short_list = [1, 2, 3]

print(list(chunks(short_list, 4)))