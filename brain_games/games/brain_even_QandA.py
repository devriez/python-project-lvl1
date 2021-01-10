import random


def generate_QandA():

    question = random.randint(0, 100)

    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'

    return(question, answer)
    