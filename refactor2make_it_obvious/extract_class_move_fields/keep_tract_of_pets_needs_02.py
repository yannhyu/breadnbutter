# keep_tract_of_pets_needs_02.py

# Start to get complicated
class Pet(object):
    def __init__(self,
                 name,
                 age,
                 *,    # This seals the args allowed
                 has_scales=False,
                 lays_eggs=False,
                 drinks_milk=False):
        self.name = name
        self.age = age
        self.treats_eaten = 0
        self.has_scales = has_scales
        self.lays_eggs = lays_eggs
        self.drinks_milk = drinks_milk

    def give_treats(self, count):
        self.treats_eaten += count

    @property
    def needs_heat_lamp(self):
        return (
            self.has_scales and 
            self.lays_eggs and
            not self.drinks_milk) 


if __name__ == '__main__':
    pet = Pet('Gregory the Gila',
              3,
              has_scales=True,
              lays_eggs=True)
    pet.give_treats(2)
    print(f'{pet.name} is {pet.age} years old')
    print(f'{pet.name} ate {pet.treats_eaten} treats')
    print(f'{pet.name} needs a heat lamp? {pet.needs_heat_lamp}')
     