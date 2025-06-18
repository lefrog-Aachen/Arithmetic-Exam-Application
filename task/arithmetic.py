import random

def parse_equation(arg):
    operands = arg.split(' ')
    x = float(operands[0])
    operation = operands[1]
    y = float(operands[2])
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == '*':
        return x * y
    return None

def gen_equation():
    operations = ['+', '-', '*']
    x = random.randint(2,9)
    y = random.randint(2,9)
    op_index = random.randint(0,2)
    operand = operations[op_index]
    return f'{x} {operand} {y}'

def get_answer():
    while True:
        try:
            response = int(input())
        except(Exception):
            print('Incorrect format.')
        else:
            return response

score = 0
for i in range(5):
    equation = gen_equation()
    print(equation)
    answer = get_answer()
    if answer == parse_equation(equation):
        print('Right!')
        score += 1
    else:
        print('Wrong!')
print(f'Your mark is {score}/5.')

