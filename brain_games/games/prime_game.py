import random
from brain_games.engine import run_game
from brain_games.consts import PRIME_INSTRUCTION


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True


def get_number_and_if_prime_answer():
    number = random.randint(1, 20)
    answer = 'yes' if is_prime(number) is True else 'no'
    return number, answer


def instruction():
    return PRIME_INSTRUCTION


def run_prime_game():
    run_game(get_number_and_if_prime_answer, instruction)
