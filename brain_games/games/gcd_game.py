#!/usr/bin/env python3
import random
import math

LOWER_LIMIT = 1
UPPER_LIMIT = 50
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_values():
    random_number_one = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    random_number_two = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    question = f'{random_number_one} {random_number_two}'
    correct_answer = math.gcd(random_number_one, random_number_two)
    return str(correct_answer), question
