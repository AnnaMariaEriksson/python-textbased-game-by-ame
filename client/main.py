from client.player import Player
from methods import *
import os

p = create_new_player()
dh = create_dreamhouse()
pet = create_pets(int(p.number_of_pets))


def main():
    def hello():
        start_menu = '''
        Hi there!
        This is a textbased game in Python.
        Or perhaps just a storytelling thing?
        I don't know yet.
        '''
        print(start_menu)

    def press_enter():
        user_input = input("Press enter to continue...")
        os.system("clear")
        return user_input

    hello()
    press_enter()
    create_new_player()
    press_enter()
    create_dreamhouse()
    press_enter()
    presentation(p, dh, pet)
    press_enter()
    reading_letter(create_dreamhouse)


if __name__ == '__main__':
    main()
