#!/usr/bin/env python3

from brain_games.is_even_logic import is_even
from brain_games.welcome import welcome_user


def main():
    name = welcome_user()
    is_even(name)


if __name__ == '__main__':
    main()
