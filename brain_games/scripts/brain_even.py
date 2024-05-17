#!/usr/bin/env python3


from brain_games.welcome import welcome_user


from brain_games.games import even_game


def main():
    welcome_user(even_game)
    even_game()


if __name__ == '__main__':
    main()
