# filter_dict_with_toolz.py

from toolz import dicttoolz

loco_dict = {'id_num':'1234', 'desc':'Ford Engine',
             'cost':1200.00, 'amount':10}

validkeys = ('desc', 'amount', 'cost')

isvalidkey = lambda x: x in validkeys
short_dict = dicttoolz.keyfilter(isvalidkey, loco_dict)

isnotvalidkey = lambda x: x not in validkeys
the_other_side_dict = dicttoolz.keyfilter(isnotvalidkey, loco_dict)
print(loco_dict)
print(short_dict)
print(the_other_side_dict)