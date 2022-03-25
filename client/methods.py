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
        pets = create_pets(int(number_of_pets))

    else:
        has_pets = False
    p = Player(name, age, favorite_color, int(number_of_pets), has_pets)
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


def create_dreamhouse():
    print("Now I have a very personal question to ask. What is the house of your dreams?")
    size = ask_question("How large would it be? ")
    bedrooms = ask_question("How many bedrooms? ")
    city = ask_question("What city would it be located in. If countryside, what would the nearest town be? ")
    country = ask_question("What country will it be in? ")
    size_of_yard = ask_question("How big of a yard would you like to have? (Answer in square meters) ")
    floors = ask_question("How many floors? ")
    price = ask_question("What would it cost to build or buy? Free is not an option here. "
                         "(Answer in numbers without spaces) ")

    dh = Dreamhouse(size, bedrooms, city, country, size_of_yard, floors, price)
    return dh


def presentation(player, dreamhouse, pet):
    print(f'''
    Ok, let's sum this information up.
    Your name is {player.name} and you're {player.age} years old.
    Your favorite color is {player.favorite_color}.
    ''')
    if player.has_pets:
        if len(player.pets) > 1:
            for pet in player.pets:
                print(f"{pet.name} is {pet.age} years old, is a {pet.species}. {pet.name}'s favorite toy is {pet.favorite_toy}."
                      f"{pet.name} is the color {pet.color}.")
        else:
            print(f"Your pet's name is {pet.name} and {pet.name} is {pet.age} years old. {pet.name} is the color {pet.color} and favorite toy is {pet.favorite_toy}")

    print(f'''
    Your dream house has {dreamhouse.bedrooms} bedrooms and {dreamhouse.floors} floors.
    It's also at least {dreamhouse.size} square meters big.
    The house is located in the city of {dreamhouse.city}.
    The house of your dream has a yard that is at least {dreamhouse.size_of_yard} square meters big.
    ''')


def reading_letter(dreamhouse):
    print(f'''
    Ok, now the fun part starts.
    Imagine that you've been away from your home for a while. Like at work or on a very weird vacation.
    You've had a hard day.
    You just want to go home. 
    When you finally get there, you've gotten a letter in the mail.
    You open it. 
    The letter says:
    
    'Congrats! You've won {dreamhouse.price} SEK. You're free to do what you want with this cash, if you chose to spend it wisely.'
    
    What will you do? Spend it wisely, like for say - on your dream house? 
    Or spend it on booze and gambling? Your choice.
    
    Type in A for spending it wisely, and B for the other choice.
    ''')

    user_input = input("A or B, what will you choose? ")

    if 'A' in user_input:
        print("Yay, you win. You get to buy or build your dream house. Good choice.")
    else:
        print("You lose. I'm so disappointed... sad face and all that crap.")
        exit()
