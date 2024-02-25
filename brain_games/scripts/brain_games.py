#!/usr/bin/env/python3


import brain_games.cli


def greet():
    print('Welcome to the Brain Games!')
    brain_games.cli.welcome_user()
    


def main():
    greet()
    
if __name__ == '__main__':
    main()
