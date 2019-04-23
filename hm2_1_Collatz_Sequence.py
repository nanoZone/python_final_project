"""
Homework 2, Exercise 1
Name: Nathan Ross
Date: 2/5/2019
Description of your program:
Automate the boring stuff, page 77, The Collatz Sequence.
Write a function named collatz() that has one parameter named number.
If number is even, then collatz() should print number // 2 and return this value.
If number is odd, then collatz() should print and return 3 * number + 1.
Then write a program that lets the user type in an integer and that keeps
calling collatz() on that number until the function returns the value 1.
Convert the return value from input() to an integer with the int() function.
"""

def collatz(number):
    if (number % 2) == 0:  # checks if number is divisible by 2 and a remainder of 0
        x = int(number // 2)  # divides the number by 2
    elif number % 2 == 1:  # checks if number is divisible by 2 and a remainder of 1
        x = int(3 * number + 1)  # multiplies the number by 3 and adds 1
    print(x)  # prints the number
    return x  # returns the number


var = int(input('Enter a number\n'))  # prompts the user to enter a number and assigns to a variable

while var > 1:  # loop to recall function if number is greater than 1
    var = collatz(var)  # calls function with number input by user

'''
Enter a number
3
10
5
16
8
4
2
1
'''