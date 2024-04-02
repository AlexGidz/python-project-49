import random
from brain_games.engine import run_game
from brain_games.consts import CALC_INSTRUCTION


def get_question_and_sign():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    sign = random.choice(['+', '-', '*'])
    question = f'{num1} {sign} {num2}'

    match sign:
        case '+':
            answer = (num1 + num2)
        case '-':
            answer = (num1 - num2)
        case '*':
            answer = (num1 * num2)

    return question, str(answer)


def instruction():
    return CALC_INSTRUCTION


def run_calc_game():
    run_game(get_question_and_sign, instruction)
