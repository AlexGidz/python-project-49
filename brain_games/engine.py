import prompt
import brain_games.games.calc_game
import brain_games.games.even_game
import brain_games.games.gcd_game
import brain_games.games.prime_game
import brain_games.games.progression_game
import brain_games.consts


def run_game(func, instruction):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n'
          f'{instruction}')

    for _ in range(brain_games.consts.AMOUNT_OF_ROUNDS):
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


def run_calc_game():
    run_game(brain_games.games.calc_game.get_question_and_sign,
             brain_games.consts.CALC_INSTRUCTION)


def run_even_game():
    run_game(brain_games.games.even_game.get_question_and_even_answer,
             brain_games.consts.EVEN_INSTRUCTION)


def run_gcd_game():
    run_game(brain_games.games.gcd_game.get_question_and_gcd_answer,
             brain_games.consts.GCD_INSTRUCTION)


def run_prime_game():
    run_game(brain_games.games.prime_game.get_number_and_if_prime_answer,
             brain_games.consts.PRIME_INSTRUCTION)


def run_progression_game():
    run_game(brain_games.games.progression_game.get_progression_and_missed_num,
             brain_games.consts.PROGRESSION_INSTRUCTION)
