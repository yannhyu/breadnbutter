# use_defaultdict2group_things.py

from collections import defaultdict

city_list = [('TX','Austin'), ('TX','Houston'), ('NY','Albany'),
             ('NY', 'Syracuse'), ('NY', 'Buffalo'), ('NY', 'Rochester'), 
             ('TX', 'Dallas'), ('CA','Sacramento'), ('CA', 'Palo Alto'),
             ('GA', 'Atlanta')]


cities_by_state = defaultdict(list)
for state, city in city_list:
    cities_by_state[state].append(city)


print(['{}: {}'.format(state, ', '.join(cities)) for state, cities in cities_by_state.items()])

# Another example
names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']

names_by_number_of_letters = defaultdict(list)
for name in names:
    names_by_number_of_letters[len(name)].append(name)

print(names_by_number_of_letters)    