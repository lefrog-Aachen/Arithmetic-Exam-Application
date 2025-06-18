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
#
# calc_input  = input()
# print(parse_operation(calc_input))

operations = ['+', '-', '*']
def gen_equation():
    x = random.randint(2,9)
    y = random.randint(2,9)
    op_index = random.randint(0,2)
    operand = operations[op_index]
    return f'{x} {operand} {y}'

equation = gen_equation()
print(equation)
answer = float(input())
if answer == parse_equation(equation):
    print('Right!')
else:
    print('Wrong!')


