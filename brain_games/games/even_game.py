#!/usr/bin/env python3
import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def func_game():
    random_number = random.randint(1, 100)
    question = random_number
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question
