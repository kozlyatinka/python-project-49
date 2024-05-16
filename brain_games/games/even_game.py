#!/usr/bin/env python3
import random


import prompt


def even_game():
    name = prompt.string('May I have your name? ')
    answers_count = 0
    print(f"Hello, {name}!")
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

    for i in range(1, 4):
        number = random.randint(0, 100)
        print(f"Question: {number}")
        answer = prompt.string('Your answer: ')
        if number % 2 == 0 and answer.lower() == "yes":
            print("Correct!")
            answers_count += 1
            continue
        elif number % 2 == 0 and answer.lower() == "no":
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\n Let's try again, {name}!")
            continue
        elif number % 2 != 0 and answer.lower() == "no":
            print("Correct!")
            answers_count += 1
            continue
        elif number % 2 != 0 and answer.lower() == "yes":
            print("'yes' is wrong answer ;(. Correct answer was 'no'.\n Let's try again, {name}!")
            break
        else:
            print("Incorrect input")

    if answers_count == 3:
        print(f"Congratulations, {name}")
