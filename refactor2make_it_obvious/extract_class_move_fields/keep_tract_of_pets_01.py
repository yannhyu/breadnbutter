# keep_tract_of_pets_01.py

class Pet(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.treats_eaten = 0

    def give_treats(self, count):
        self.treats_eaten += count


if __name__ == '__main__':
    pet = Pet('Gregory the Gila', 3)
    pet.give_treats(2)
    print(f'{pet.name} is {pet.age} years old')
    print(f'{pet.name} ate {pet.treats_eaten} treats')
     