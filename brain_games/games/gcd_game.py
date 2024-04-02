import random
from brain_games.engine import run_game
from brain_games.consts import GCD_INSTRUCTION
from math import gcd


def get_question_and_gcd_answer():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    question = f'{num1} {num2}'
    answer = str(gcd(num1, num2))
    return question, answer


def instruction():
    return GCD_INSTRUCTION


def run_gcd_game():
    run_game(get_question_and_gcd_answer, instruction)
