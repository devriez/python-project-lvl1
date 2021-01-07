import prompt
import random



def is_even(user_name):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    counter = 0

    for i in range(3):
        qustion_number = random.randint(0, 100)

        if qustion_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        print('Qustion: ', qustion_number)
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {user_name}!")
            break
        counter += 1

    if counter == 3:
        print(f'Congratulations, {user_name}!')
