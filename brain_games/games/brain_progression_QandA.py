import random


def generate():
    head_question = 'What number is missing in the progression?'
    length = random.randint(6, 16)
    position = random.randint(1, length)
    step = random.randint(2, 10)
    start = random.randint(0, 20)
    finish = start + length * step
    progression = [str(x) for x in range(start, finish, step)]
    answer = progression[positioin]
    progression[position] = '..'
    question = ' '.join(progression)

    return(head_question, question, str(answer))