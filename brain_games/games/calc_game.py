#!/usr/bin/env python3
import random


DESCRIPTION = 'What is the result of the expression?'


def func_game():
    random_number_one = random.randint(1, 100)
    random_number_two = random.randint(1, 100)
    random_operator = random.choice('+-*')
    question = f'{random_number_one} {random_operator} {random_number_two}'
    correct_answer = str(calculate(random_number_one, random_number_two, random_operator))
    return question, correct_answer
                         
 
def calculate(random_number_one, random_number_two, random_operator):
    if random_operator == '*':
        result = random_number_one * random_number_two
    elif random_operator == '+':
        result = random_number_one + random_number_two
    elif random_operator == '-':
        result = random_number_one - random_number_two
    return result