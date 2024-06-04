#!/usr/bin/env python3
import random

LOWER_LIMIT = 1
STEP_UPPER_LIMIT = 3
UPPER_LIMIT = 20
MIN_LENGTH = 5
MAX_LENGTH = 15
DESCRIPTION = 'What number is missing in the progression?'


def get_values():
    initial_term = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    common_difference = random.randint(LOWER_LIMIT, STEP_UPPER_LIMIT)
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    progression = get_progression(initial_term, common_difference, length)
    random_answer_index = random.randint(LOWER_LIMIT, len(progression) - 1)
    correct_answer = str(progression[random_answer_index])
    progression[random_answer_index] = ".."
    question = ' '.join(map(str, progression))
    return correct_answer, question


def get_progression(initial_term, common_difference, length):
    number_list = []
    random_step = random.randint(LOWER_LIMIT, STEP_UPPER_LIMIT)
    end_progression = initial_term + (length * random_step)
    for number in range(initial_term, end_progression, common_difference):
        number_list.append(number)
    return number_list
