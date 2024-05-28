#!/usr/bin/env python3
import random

LOWER_LIMIT = 1
STEP_UPPER_LIMIT = 4
UPPER_LIMIT = 20
DESCRIPTION = 'What number is missing in the progression?'


def get_values():
    progression = get_progression(LOWER_LIMIT, UPPER_LIMIT, STEP_UPPER_LIMIT)
    random_answer_index = random.randint(LOWER_LIMIT, len(progression) - 1)
    correct_answer = str(progression[random_answer_index])
    progression[random_answer_index] = ".."
    question = ' '.join(map(str, progression))
    return correct_answer, question


def get_progression(LOWER_LIMIT, UPPER_LIMIT, STEP_UPPER_LIMIT):
    number_list = []
    random_step = random.randint(LOWER_LIMIT, STEP_UPPER_LIMIT)
    for number in range(LOWER_LIMIT, UPPER_LIMIT, random_step):
        number_list.append(number)
    return number_list
