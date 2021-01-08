import random


def generate():
    head_question = 'What is the result of the expression?'
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

    return(head_question, question, str(answer))
