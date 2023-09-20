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
