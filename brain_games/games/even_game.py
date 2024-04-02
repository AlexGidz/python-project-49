import random
from brain_games.engine import run_game
from brain_games.consts import EVEN_INSTRUCTION


def if_even_num(num):
    if num % 2 == 0:
        return True
    else:
        return False


def get_question_and_even_answer():
    question = random.randint(1, 100)

    def answer():
        return 'yes' if if_even_num(question) is True else 'no'
    answer = answer()
    return question, answer


def instruction():
    return EVEN_INSTRUCTION


def run_even_game():
    run_game(get_question_and_even_answer, instruction)
