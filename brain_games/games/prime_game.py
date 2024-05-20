#!/usr/bin/env python3
import random

DESCRIPTION = 'Answer "yes" if the number is is prime, otherwise answer "no".'


def func_game():
    random_number = random.randint(1, 100)
    question = random_number
    if random_number > 1:
        for i in range(2, (random_number // 2) + 1):
            if random_number % i == 0:
                correct_answer = 'no'
            else:
                correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question
