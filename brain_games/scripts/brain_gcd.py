#! /usr/bin/env python3


import brain_games.game_engine
from brain_games.games.brain_gcd_QandA import generate
from brain_games.welcome import welcome_user


def main():
    name = welcome_user()
    game_engine.mane(generate, name)


if name == '__name__':
    main()