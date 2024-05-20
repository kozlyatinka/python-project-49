#!/usr/bin/env python3
import random


DESCRIPTION = 'FWhat number is missing in the progression?'


def func_game():
    progression = get_progression()
    random_answer_index = random.randint(1, len(progression) - 1)
    correct_answer = str(progression[random_answer_index])
    progression[random_answer_index] = ".."
    question = ' '.join(map(str, progression))
    return correct_answer, question

def get_progression():
    number_list = []
    random_step = random.randint(1, 3)
    for number in range(1, 11, random_step):
        number_list.append(number)
    return number_list
