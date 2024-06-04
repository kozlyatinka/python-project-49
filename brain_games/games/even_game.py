#!/usr/bin/env python3
import random

LOWER_LIMIT = 1
UPPER_LIMIT = 200
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_values():
    random_number = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    question = random_number
    if is_even(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question


def is_even(random_number):
    return random_number % 2 == 0
