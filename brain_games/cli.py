import prompt


def launch():
    name = prompt.string('May I have your name? ')
    return print(f'Hello, {name}!')
