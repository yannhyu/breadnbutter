# when2use_namedtuple.py

from collections import namedtuple

Animal = namedtuple('Animal', ['name', 'age', 'type'])

perry = Animal(name='perry', age=31, type='cat')
print('{} the {}..'.format(perry.name, perry.type))

#Strange looking but works too
Animal = namedtuple('Animal', 'name age type')
steve = Animal(name='steve', age=1, type='dog')
print('{} the {}...'.format(steve.name, steve.type))

# can convert a namedtuple to a dictionary
perry_ordereddict = perry._asdict()
print(perry_ordereddict)