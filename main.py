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


def valid_op(user_prompt):
    while True:
        user_input = input(user_prompt)

        if user_input in ['+', '-', '*', '/']:
            return user_input
        else:
            print('invalid operation input.')


def get_int(user_prompt):
    while True:
        user_input = input(user_prompt)

        if user_input.lstrip('-').isdigit():
            return int(user_input)
        else:
            print('invalid input value.')


def display(value_list, operator_list):
    print(f"Entered expression:{value_list[0]}{operator_list[0]}{value_list[1]}{operator_list[1]}{value_list[2]}")
    result = evaluate(value_list, operator_list)
    print(f"Your final answer:{result}")


if __name__ == "__main__":
    value = []
    operator = []
    value.append(get_int("Enter the first value:"))
    operator.append(valid_op("Enter the first operator:"))
    value.append(get_int("Enter the second value:"))
    operator.append(valid_op("Enter the second operator:"))
    value.append(get_int("Enter the third value:"))
    display(value, operator)
