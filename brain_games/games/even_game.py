#!/usr/bin/env python3
import random


import prompt


import welcome


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_game():
    answers_count = 0
    while answers_count < 3:
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if answer.lower() == correct_answer:
            print('Correct!')
            answers_count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {welcome.name}!")
            break

    if answers_count == 3:
        print(f"Congratulations, {welcome.name()}")
