#!/usr/bin/env python3
from brain_games.welcome import welcome_user
from brain_games.games import even_calc


def main():
    welcome_user(even_calc)


if __name__ == '__main__':
    main()