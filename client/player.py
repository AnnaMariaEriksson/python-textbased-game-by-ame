from client.dreamhouse import Dreamhouse


class Player:
    def __init__(self, name, age, favorite_color, number_of_pets, has_pets = False):
        self.name = name
        self.age = age
        self.favorite_color = favorite_color
        self.number_of_pets = number_of_pets
        self.has_pets = has_pets
        self.pets = []


