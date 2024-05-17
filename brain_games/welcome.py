import prompt


def welcome_user(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    return name
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
