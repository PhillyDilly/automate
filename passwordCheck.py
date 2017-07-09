'''
################################################################################
# Name: passwordCheck.py
# Date: 7/8/2017
# Revision: 1.0
################################################################################

Automate the Boring Stuff: Chapter 7, Project 1
Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that is at
least eight characters long, contains both uppercase and lowercase characters,
and has at least one digit. You may need to test the string against multiple
regex patterns to validate its strength

'''

import re
import sys

def checkLength(password):

    if len(password) > 0:                   # Check to ensure imput was not null

        print('Passed: password was at least entered.')

        if len(password) >= 8:              # Check if password is at lest 8 char long

            print('Passed: password was 8 characters long.')

        else:

            print('Failed: password was not eight characters long.')
            sys.exit(1)                     # Exit program

    else:

        print('Failed: password was null')
        sys.exit(1)                         # Exit program


def checkText(password):

    textCheck = re.compile(r'\w')

    if textCheck.search(password):

        print('Passed: password contains text.')

    else:

        print('Failed: password does not contain text.')

def checkLowerUpper(password):

    lowAndUp = re.compile(r'[a-zAZ]')

    if lowAndUp.search(password):

        print('Passed: password contains both upper and lower case characters.')

    else:

        print('Failed: password does not contain both lower and upper case characters.')



def checkNumbers(password):

    numCheck = re.compile(r'\d')

    if numCheck.search(password):

        print('Passed: password contains numbers.')

    else:

        print('Print: password does not contain any numbers')



def checkSpecial(password):

    specCheck = re.compile(r'\d')

    if specCheck.search(password):

        print('Passed: password contains special characters.')

    else:

        print('Print: password does not contain any special characters.')


password = input('Enter a password to be checked: ')

checkLength(password)
checkText(password)
checkLowerUpper(password)
checkNumbers(password)
checkSpecial(password)

