import random


def generate_QandA():
    length = random.randint(6, 16)
    position = random.randint(0, length)
    step = random.randint(2, 10)
    start = random.randint(0, 20)
    finish = start + (length + 1) * step
    progression = [str(x) for x in range(start, finish, step)]
    answer = progression[position]
    progression[position] = '..'
    question = ' '.join(progression)

    return(question, str(answer))
