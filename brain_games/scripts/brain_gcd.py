#! /usr/bin/env python3


from brain_games.game_engine import ask_and_check_answer
from brain_games.games.brain_gcd_QandA import generate_QandA
from brain_games.welcome import welcome_user


def main():
    user_name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    ask_and_check_answer(generate_QandA, user_name)


if __name__ == '__mane__':
    main()
