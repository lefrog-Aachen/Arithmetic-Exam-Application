def parse_operation(arg):
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

calc_input  = input()
print(parse_operation(calc_input))



