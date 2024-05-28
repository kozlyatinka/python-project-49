#!/usr/bin/env python3
import random
LOWER_LIMIT = 1
UPPER_LIMIT = 200

DESCRIPTION = 'What is the result of the expression?'


def get_values():
    random_one = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    random_two = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    random_operator = random.choice('+-*')
    question = f'{random_one} {random_operator} {random_two}'
    correct_answer = str(calculate(random_one, random_two, random_operator))
    return correct_answer, question


def calculate(random_one, random_two, random_operator):
    if random_operator == '*':
        result = random_one * random_two
    elif random_operator == '+':
        result = random_one + random_two
    elif random_operator == '-':
        result = random_one - random_two
    return result
