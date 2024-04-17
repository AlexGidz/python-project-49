import random
from math import gcd
GCD_INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    question = f'{num1} {num2}'
    answer = str(gcd(num1, num2))
    return question, answer, GCD_INSTRUCTION


def gcd_game():
    return get_question_and_answer()
