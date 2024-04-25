import random
from brain_games.consts import MIN_PROGRESSION_LENGTH
from brain_games.consts import MAX_PROGRESSION_LENGTH
INSTRUCTION = 'What number is missing in the progression?'


def get_question_and_answer():
    prog_start, prog_step = random.randint(1, 10), random.randint(1, 10)
    prog_length = random.randint(MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)
    missed_index = random.randint(0, prog_length - 1)

    progression = []
    for i in range(prog_length):
        progression.append(prog_start + prog_step * i)

    missed_num = progression[missed_index]
    progression[missed_index] = '..'
    progression_with_missed_num = ' '.join(map(str, progression))

    return progression_with_missed_num, str(missed_num)
