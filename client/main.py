from client.player import Player
from methods import *
import os


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


if __name__ == '__main__':
    main()
