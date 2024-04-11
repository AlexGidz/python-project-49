import prompt
from brain_games.consts import AMOUNT_OF_ROUNDS


def run_game(func, instruction):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n'
          f'{instruction}')

    for _ in range(AMOUNT_OF_ROUNDS):
        question, correct_answer = func()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
        else:
            print(f'"{answer}" is wrong answer ;(. '
                  f'Correct answer was "{correct_answer}"\n'
                  f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
