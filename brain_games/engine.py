import prompt

ROUNDS = 3


def launch(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    answers_count = 0
    while answers_count < ROUNDS:
        correct_answer, question = game.get_values()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if not answer:
            print("Enter the answer")
        elif answer.lower() == correct_answer:
            print('Correct!')
            answers_count += 1
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

    if answers_count == ROUNDS:
        print(f"Congratulations, {name}!")
