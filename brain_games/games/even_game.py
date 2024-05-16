#!/usr/bin/env python3
import random


import prompt


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def even_game(game):
    name = prompt.string('May I have your name? ')
    answers_count = 0
    print(f"Hello, {name}!")

    for i in range(1, 4):
        number = random.randint(0, 100)
        print(f"Question: {number}")
        answer = prompt.string('Your answer: ').lower()
        if (number % 2 == 0 and answer == "yes") or (number % 2 != 0 and answer == "no"):
            print("Correct!")
            answers_count += 1
            continue
        elif (number % 2 == 0 and answer == "no") or (number % 2 != 0 and answer == "yes"):
            if answer == "no":
                correct_answer = "yes"
            if answer == "yes":
                correct_answer = "no"
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
            
        else:
            print("Incorrect input")

    if answers_count == 3:
        print(f"Congratulations, {name}")
