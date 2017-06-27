# move_fields2inner_obj_04.py
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
                 animal=None,    # Optional param
                 **kwargs):
        # Either the new way or the old, not both
        if kwargs and animal is not None:
            raise TypeError('Mixed up usage not allowed')
        # Must be using the old way, issue warning for now
        if animal is None:
            warnings.warn('Ought to use Animal')
            # Ensure backward compatibility
            animal = Animal(**kwargs)
        self.name = name
        self.age = age
        self.treats_eaten = 0
        self.animal = animal
    
    # For backward compatibility
    @property
    def has_scales(self):
        warnings.warn('Use animal attribute')
        return self.animal.has_scales

    # For backward compatibility
    @property
    def lays_eggs(self):
        warnings.warn('Use animal attribute')
        return self.animal.lays_eggs

    # For backward compatibility
    @property
    def drinks_milk(self):
        warnings.warn('Use animal attribute')
        return self.animal.drinks_milk

    @property
    def needs_heat_lamp(self):
        return (
            self.has_scales and 
            self.lays_eggs and
            not self.drinks_milk)

    def give_treats(self, count):
        self.treats_eaten += count

if __name__ == '__main__':
    # New attributes don't warn
    animal = Animal(has_scales=True,
                    lays_eggs=True)

    pet = Pet('Gregory the Gila',
              3,
              animal)

    print(f'{pet.name} has scales ? {pet.animal.has_scales}')
                