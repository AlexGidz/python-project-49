import random


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
