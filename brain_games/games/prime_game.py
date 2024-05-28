#!/usr/bin/env python3
import random

LOWER_LIMIT = 1
UPPER_LIMIT = 50
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def func_game():
    random_number = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    question = random_number
    if prime(random_number):
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return correct_answer, question


def prime(random_number):
    if random_number > 1:
        for i in range(2, random_number):
            if random_number % i == 0:
                return False
            else:
                return True
    else:
        return False
