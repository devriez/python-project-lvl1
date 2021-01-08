#!/usr/bin/env python3


import brain_games.game_engine.main
from brain_games.games.brain_calc_QandA import generate
from brain_games.welcome import welcome_user


def main():
    name = welcome_user()
    brain_games.game_engine.main(generate, name)


if __name__ == '__main__':
    main()
