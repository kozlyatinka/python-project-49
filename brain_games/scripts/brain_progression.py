#!/usr/bin/env python3
from brain_games.welcome import welcome_user
from brain_games.games import progression_game


def main():
    welcome_user(progression_game)


if __name__ == '__main__':
    main()
