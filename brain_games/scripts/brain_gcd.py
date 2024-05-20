#!/usr/bin/env python3
from brain_games.welcome import welcome_user
from brain_games.games import gcd_game


def main():
    welcome_user(gcd_game)


if __name__ == '__main__':
    main()
