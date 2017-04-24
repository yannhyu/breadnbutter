# sub_dict.py

loco_dict = {'id_num':'1234', 'desc':'Ford Engine',
             'cost':1200.00, 'amount':10}

validkeys = ('desc', 'amount', 'cost')

short_dict = {vkey: loco_dict[vkey] for vkey in validkeys }
print(short_dict)


short_dict = { vk: vv  for vk, vv in loco_dict.items() if vk in validkeys }
print(short_dict)


# Not that clear but works
# .items() is a list of (k, v) tuples
short_dict = dict(filter(lambda i:i[0] in validkeys, loco_dict.items()))
print(short_dict)

for vi in loco_dict.items():
    print(vi)