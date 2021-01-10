import random


def isPrime(a):
    return all(a % i for i in range(2, a))


def generate_QandA():
    number = random.randint(1, 10)
    question = f'{number}'
    answer = 'yes' if isPrime(number) else 'no'

    return(question, answer)
