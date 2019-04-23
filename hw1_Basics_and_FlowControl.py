import random

'''
Homework 1, Exercise 1
Name: Nathan Ross
Date: Jan 31, 2019
Description: Python basics and flow control. 
This program that has a secret program inside a math calculation program.
The user is prompted to input their name. If their name is anything besides 'Ellie'
the program will prompt them to enter two numbers to add, subtract and multiply
If the user's name is 'Ellie', the user will be prompted to answer three security
questions. If she can answer the answers correctly, the program will tell here what
her birthday present is and it goes into asking her about guests for her 
birthday party.  
'''


def add(p, q):
    return p + q  # addition operator


def sub(r, s):
    return r - s  # subtraction operator


def multiply(t, u):
    return t * u  # multiplication operator


correctAnswers = 0  # #### int variable ####
age = 0
# Block 1 Starts = While loop, 3 security questions in a for loop, tally correct answers
while True:
    name = (input('What is your name\n'))
    if name == 'Ellie':
        print('Hey there ' + name + '!\nI made this program for your birthday.')
        print('But, I need to be sure it\'s really you!')
        print('If you can answer these 3 security questions, I\'ll tell you what we got you for your birthday.\n')
        i = 0
        '''
        This is the for loop to ask 3 security questions with the range()
        The value of the iterator is used in asking the 3 questions
        '''
        for i in range(1, 4):  # #### Loop for 3 questions using range() ####
            if i == 1:  # #### Value of iterator is used to ask 3 questions ####
                print('Question ' + str(i) + ':')  # #### str() ####
                print('How many letters are in your middle name?')
                middleName = 'Grace'
                # print('FOR DAMIA= ANSWER:  5')
                solutionQuestion1 = (len(middleName))  # #### len() ####
                answerQuestion1 = int(input())  # #### int() ####
                if answerQuestion1 == solutionQuestion1:
                    correctAnswers += 1
            elif i == 2:
                print('Question ' + str(i) + ':')
                print('If it\'s really you, how do you respond when I call you a cutie PI?')
                # print('FOR DAMIA= ANSWER:   3.14')
                answerQuestion2 = float(input())  # #### float() ####
                solutionQuestion2 = 3.14  # ### float variable ####
                if answerQuestion2 == solutionQuestion2:
                    correctAnswers += 1
            elif i == 3:
                print('Question ' + str(i) + ':')
                print('What month is your birthday?')
                # print('FOR DAMIA= ANSWER:  February')
                answerQuestion3 = str(input())  # #### str() ####
                solutionQuestion3 = 'February'  # #### string variable ####
                if answerQuestion3 == solutionQuestion3:
                    correctAnswers += 1

            i += 1  # as number increments through loop it triggers if statements and iterator printed with questions
    break
# Block 1 Ends

# Block 2 Starts
'''
This section of the code is based on how many correct answers the user gave.
If there are zero correct answers, it is because the user entered any name besides the correct name.
If there are zero correct answers, the user is taken through a very simple math calculation program.
If the user enters the correct name, but answers 1 or 2 questions wrong, then they are not given the
secret message and the program ends. If the user uses the correct name and answers correctly all three
questions, the user is given a secret message and prompted through a few more questions.
'''
if correctAnswers == 0:  # Basic math shell program if specific user name isn't answered
    print('Hey there ' + name + '!')
    print('In this program, we are going to calculate 2 numbers with addition, subtraction and multiplication.')
    print('\nLet\'s do some math!!!')
    a = float(input('Enter the first number\n'))
    b = float(input('Enter the second number\n'))
    print('These two numbers added together are ' + str(add(a, b)))
    print('These two numbers subtracted together are ' + str(sub(a, b)))
    print('These two numbers multiplied together are ' + str(multiply(a, b)))
elif correctAnswers == 1:
    print('You answered 2 wrong. Sorry. Your present remains a mystery Goodbye!!!')
elif correctAnswers == 2:
    print('You answered 1 wrong. Sorry. Your present remains a mystery Goodbye!!!')
elif correctAnswers == 3:
    dollars = random.randint(25, 51)
    costOfBicycle = 150
    cashOnly = costOfBicycle + dollars
    print('\nSo, you have two options:')  # ##### SECRET INFORMATION #####
    print('The first option is a bicycle and $' + str(dollars) + '\n OR')
    print('Just money: $' + str(cashOnly))

    print('\nDo you remember how many friends we said you can invite to your party?')
    # BLOCK 3 STARTS =  While statement incorporating if,elif,break,coninue... else used in truthy/falsey below
    while True:
        numOfGuests = int(input())
        if numOfGuests == 5:
            print('You are right! You can have up to 5 friends at the party\n')
            break
        elif numOfGuests < 5:
            print('You can have more friends than that. Try again!')
            continue
        elif numOfGuests < 10:
            numOfGuests = (numOfGuests % 5)  # #### modulus operator ####
            print('That\'s ' + str(numOfGuests % 5) + ' friends too many! Try again!')
            continue
        elif numOfGuests >= 10:
            print('You\'re definitely not having that many people over. Try again! ')
            continue

    #  ####"Truthy and Falsey" ####
    numOfBrothersInvited = int(input('How many of your four brothers are welcome to join the party?\n'))
    if numOfBrothersInvited:
        print('That is nice of you. Maybe they will buy you presents, too.\n')
        print('Well, see you at the party\nHappy Birthday\nGoodbye until then\nLOVE YOU!!!')
    else:
        print('You might want to invite them because they could bring you presents.')
        print('Well, see you at the party\nHappy Birthday\nGoodbye until then\nLOVE YOU!!!')
    # BLOCK 3 ENDS
print('\nEnd of program. Have a nice day')
# BLOCK 2 ENDS
