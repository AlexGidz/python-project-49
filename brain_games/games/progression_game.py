import random
from brain_games.engine import run_game
from brain_games.consts import MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH, PROGRESSION_INSTRUCTION


def get_progression_and_missed_num():
    progression_start, progression_step = random.randint(1, 10), random.randint(1, 10)
    progression_length = random.randint(MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)
    missed_index = random.randint(0, progression_length - 1)

    progression = []
    for i in range(progression_length):
        progression.append(progression_start + progression_step * i)

    missed_num = progression[missed_index]
    progression[missed_index] = '..'
    progression_with_missed_num = ' '.join(map(str, progression))

    return progression_with_missed_num, str(missed_num)


def instruction():
    return PROGRESSION_INSTRUCTION


def run_progression_game():
    run_game(get_progression_and_missed_num, instruction)
