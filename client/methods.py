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
    i = 0
    while i < number_of_pets:
        print("Ok, you have pets. Let's add them, shall we?")
        name = ask_question("What is your pet's name?")
        age = ask_question("How old is your pet? (write it with a number)")
        species = ask_question("What kind of pet is it? (like dog, cat, bird etc)")
        color = ask_question("What color is your pet's fur?")
        favorite_toy = ask_question("What is the pet's favorite toy?")

        new_pet = Pet(name, age, species, color, favorite_toy)
        list_of_pets.append(new_pet)
        i += 1
    return list_of_pets


def create_dreamhouse():
    print("Now I have a very personal question to ask. What is the house of your dreams?")
    size = ask_question("How large would it be? ")
    bedrooms = ask_question("How many bedrooms? ")
    city_or_countryside = ask_question("Will it be located in a city or in the countryside? ")
    if 'city' in city_or_countryside:
        city = city_or_countryside
    else:
        city = None
        countryside = True
    country = ask_question("What country will it be in? ")
    has_yard = ask_question("Will it have a yard? ")
    if 'yes' in has_yard:
        has_yard = True
        size_of_yard = ask_question("How big of a yard would you like to have? Answer in square meters")
        floors = ask_question("How many floors? ")
        price = ask_question("What would it cost to build or buy? Free is not an option here.")
    else:
        has_yard = False

    dh = Dreamhouse(size, bedrooms, city, country, countryside, size_of_yard, floors, price, has_yard)
    return dh
