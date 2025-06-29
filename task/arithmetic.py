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
        except Exception:
            print('Incorrect format.')
        else:
            return response

lvl = None
lvl_description = ['simple operations with numbers 2-9', 'integral squares 11-29']
while True:
    print('Which level do you want? Enter a number:')
    print(f'1 - {lvl_description[0]}')
    print(f'2 - {lvl_description[1]}')
    level = input()
    if level == '1':
        eq_lvl = 0
        break
    elif level == '2':
        eq_lvl = 1
        break
    else:
        print('Incorrect Format.')

score = 0
for i in range(5):
    if eq_lvl == 0:
        equation = gen_equation()
        print(equation)
        answer = get_answer()
        if answer == parse_equation(equation):
            print('Right!')
            score += 1
        else:
            print('Wrong!')
    elif eq_lvl == 1:
        int_number = random.randint(11,29)
        print(int_number)
        answer = get_answer()
        if answer == int_number ** 2:
            print('Right!')
            score += 1
        else:
            print('Wrong!')

print(f'Your mark is {score}/5. Would you like to save the result? Enter yes or no.')
response = input().lower()
if response == 'yes' or response == 'y':
    user_name = input('What is your name?')
    with open('results.txt', 'a') as file:
        file.write(f'{user_name}: {score}/5 in level {eq_lvl + 1} ({lvl_description[eq_lvl]}).\n')
    print('The results have been saved in "results.txt"')

