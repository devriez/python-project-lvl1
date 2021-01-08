#! /usr/bin/env python3


import brain_games.game_engine
from brain_games.games.brain_prime_QandA import generate
from brain_games.welcome import welcome_user


def main():
    name = welcome_user()
    brain_games.game_engine.main(generate, name)


if __name__ == '__mane__':
    main()