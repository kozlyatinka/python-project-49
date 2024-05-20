#!/usr/bin/env python3
import random


DESCRIPTION = 'What is the result of the expression?'


def func_game():
    random_one = random.randint(1, 100)
    random_two = random.randint(1, 100)
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
