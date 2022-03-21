def main():
    def hello():
        start_menu = '''
        Hi there!
        This is a textbased game in Python.
        Or perhaps just a storyboard?
        I don't know yet.
        '''
        return start_menu
    def get_player_name():
        player_name = input("What is your name?")
        return f"Hello, {player_name}! Nice of you to join us."
    
    print(hello())
    print(get_player_name())

if __name__ == '__main__':
    main()