# Example of recursion using Python to compute factorials
"""
0! = 1
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
"""


def factorial(number):

    if number == 1:
        #print('Number is: ' + str(number))
        return number

    else:
        #print('Number is: ' + str(number))
        return number * factorial(number - 1)

print('Factorial of 10 is: ' + str(factorial(10)))

