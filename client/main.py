from client.player import Player
from methods import *


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
        # print("\033")

        return user_input

    hello()
    press_enter()
    create_new_player()

if __name__ == '__main__':
    main()
