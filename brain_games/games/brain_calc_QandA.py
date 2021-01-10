import random


def generate_QandA():
    operations = {1: '+', 2: "-", 3: "*"}
    operand1 = random.randint(1, 100)
    operand2 = random.randint(1, 100)
    operation = operations[random.randint(1, 3)]
    question = f'{operand1} {operation} {operand2}'

    if operation == '+':
        answer = operand1 + operand2
    elif operation == '-':
        answer = operand1 - operand2
    else:
        answer = operand1 * operand2

    return(question, str(answer))
