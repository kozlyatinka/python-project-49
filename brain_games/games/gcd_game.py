#!/usr/bin/env python3
import random
import math


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def func_game():
    random_number_one = random.randint(1, 100)
    random_number_two = random.randint(1, 100)
    question = f'{random_number_one} {random_number_two}'
    correct_answer = math.gcd(random_number_one, random_number_two)
    return correct_answer, question
