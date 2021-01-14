import prompt


def welcome_user():
    '''
    Ask user name and display greetings
    return: name: user name
    '''
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name, '!')
    return(name)
