import prompt
AMOUNT_OF_ROUNDS = 3


def run_game(get_question_and_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n'
          f'{get_question_and_answer()[2]}')

    for _ in range(AMOUNT_OF_ROUNDS):
        question, correct_answer, _ = get_question_and_answer()
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
