import random
INSTRUCTION = (
    'Answer "yes" if given number is prime. '
    'Otherwise answer "no".'
)


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True


def get_question_and_answer():
    number = random.randint(1, 20)
    answer = 'yes' if is_prime(number) is True else 'no'
    return number, answer
