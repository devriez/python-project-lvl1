import prompt


def main(game, user_name):
    (head_question, question, correct_answer) = game()

    print(head_question)

    counter = 0

    for i in range(3):
        (_, question, correct_answer) = game()

        print('Question: ', question)
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print("Correct!")
        else:
            print(f''''"{answer}" is wrong answer ;(.
Correct answer was "{correct_answer}"''')
            print(f"Let's try again, {user_name}!")
            break

        counter += 1

    if counter == 3:
        print(f'Congratulations, {user_name}!')
