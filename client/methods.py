from client.pet import Pet
from client.player import *


def yes_no_validator(answer):
    return True


def create_new_player():
    print("""Now, we're gonna store your info. 
    Don't worry, it's totally safe. 
    Trust me. This is a simple console application. 
    Nothing is stored here.""")
    name = ask_question("What is your name? ")
    age = ask_question("How old are you? ")
    favorite_color = ask_question("What is your favorite color? ")
    has_pets = ask_question("Do you have any pets? ", yes_no_validator)
    if 'yes' in has_pets:
        has_pets = True
        number_of_pets = ask_question("How many pets do you have? ")
        create_pets(int(number_of_pets))
        pets = create_pets(int(number_of_pets))

    else:
        has_pets = False
    p = Player(name, age, favorite_color, number_of_pets, has_pets)
    p.pets.append(pets)
    return p


def ask_question(question, validator=None):
    answer = input(question)
    if validator is not None:
        if validator(answer):
            return answer
        else:
            print("Something went wrong")
            return None
    return answer


def create_pets(number_of_pets):
    list_of_pets = []

    for pet in range(number_of_pets):
        print("Ok, you have pets. Let's add them, shall we?")
        name = ask_question("What is your pet's name?")
        age = ask_question("How old is your pet? (write it with a number)")
        species = ask_question("What kind of pet is it? (like dog, cat, bird etc)")
        color = ask_question("What color is your pet's fur?")
        favorite_toy = ask_question("What is the pet's favorite toy?")

        new_pet = Pet(name, age, species, color, favorite_toy)
        list_of_pets.append(new_pet)
    return list_of_pets
