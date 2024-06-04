#!/usr/bin/env python3
import random

LOWER_LIMIT = 1
UPPER_LIMIT = 50
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_values():
    random_number = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    question = random_number
    if not is_prime(random_number):
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return correct_answer, question


def is_prime(random_number):
    if random_number < 2 or random_number % 2 == 0:
        return False
    for i in range(3, int(random_number ** 0.5) + 1, 2):
        if random_number % i == 0:
            return False
    return True
