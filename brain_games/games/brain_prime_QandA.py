import random

def isPrime(a):
    return all(a % i for i in range(2, a))

def generate():
    head_question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    number = random.randint(1, 10)
    question = f'{number}'
    answer = 'yes' if isPrime(number) else 'no'

    return(head_question, question, answer)
