#!/usr/bin/env/python3
from brain_games.engine import run_game
from brain_games.games.progression_game import progression_game


def main():
    run_game(progression_game)


if __name__ == '__main__':
    main()
