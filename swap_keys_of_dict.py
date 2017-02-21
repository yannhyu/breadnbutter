# swap_keys_of_dict.py
import collections

aday = collections.OrderedDict()
aday['breakfast'] = '2 pancakes'
aday['lunch'] = '3 slices of pizza'
aday['dinner'] = 'pasta & salad'

print(aday)
print(aday.values())
print(aday.keys())

new_keys = ['le petit dejeuner', 'le dejeuner', 'le diner']

un_jour = collections.OrderedDict(zip(new_keys, aday.values()))
print(un_jour)

# most of the we can get away with a plain dict
un_jour_ordinaire = dict(zip(new_keys, aday.values()))
print(un_jour_ordinaire)
