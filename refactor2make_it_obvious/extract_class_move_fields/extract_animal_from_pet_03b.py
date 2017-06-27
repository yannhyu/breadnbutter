# extract_animal_from_pet_03b.py
import warnings

class Animal(object):
    def __init__(self,
                 *,
                 has_scales=False,
                 lays_eggs=False,
                 drinks_milk=False):
        self.has_scales = has_scales
        self.lays_eggs = lays_eggs
        self.drinks_milk = drinks_milk

class Pet(object):
    def __init__(self,
                 name,
                 age,
                 animal=None,    # This makes it an optional param
                 **kwargs):
        # Either the new way or the old, not both
        if kwargs and animal is not None:
            raise TypeError('Mixed up usage not allowed')
        # Must be using the old way, issue warning for now    
        if animal is None:
            warnings.warn('Ought to use Animal')
            animal = Animal(**kwargs)
        self.name = name
        self.age = age
        self.treats_eaten = 0
        self.animal = animal

    def give_treats(self, count):
        self.treats_eaten += count

    @property
    def needs_heat_lamp(self):
        return (
            self.has_scales and 
            self.lays_eggs and
            not self.drinks_milk)


if __name__ == '__main__':
    # animal = Animal(has_scales=True,
    #                 lays_eggs=True)

    # Old constructor works, but warns
    pet = Pet('Gregory the Gila',
              3,
              has_scales=True,
              lays_eggs=True)

"""
extract_animal_from_pet_04.py:23: UserWarning: Ought to use Animal
  warnings.warn('Ought to use Animal')
"""                   