"""
Remember to follow these coding standards:
Put a space( ) after comma(,)
Put a space before and after assignment(=) and comparison(==, !=, etc.)
Put a space before and after arithmetic operators(+, -, *, /, etc.)
Don't put a space at the end of a line
Leave 2 blank lines between functions
Leave 1 blank line at the end of the file
"""


def operation(operator, a, b):
    if operator == '+':
        return myAdd(a, b)
    elif operator == '-':
        return mySub(a, b)
    elif operator == '*':
        return myMul(a, b)
    elif operator == '/':
        return myDiv(a, b)
    else:
        print(f'Operation {operator} is not allowed')


def evaluate(number_list, operation_list):
    if operation_list[0] in ('+', '-') and operation_list[1] in ('*', '/'):
        temp = operation(operation_list[1], number_list[1], number_list[2])
        return operation(operation_list[0], number_list[0], temp)
    else:
        temp = operation(operation_list[0], number_list[0], number_list[1])
        return operation(operation_list[1], temp, number_list[2])
    

def myAdd(a, b):
    return a + b

def mySub(a, b):
    return a - b

def myMul(a, b):
    return a * b

def myDiv(a, b): 
    if b != 0:
        return a // b
    else:
        return "division by zero is not allowed."

def validint(val):
    while True:
        user_input = input(val)
    
    if user_input.lstrip('-').isdigit():
        return int(user_input)
    else:
        print('invalid input value.')
