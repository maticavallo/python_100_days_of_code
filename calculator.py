def add(n1, n2):
    return n1 + n2
def substract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1*n2
def division(n1, n2):
    return n1/n2

math_operations = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': division,

}
def calculator():
    n1 = float(input(f'Welcome to the Calculator!\nWhat\'s your first number?: '))
    shouldcontinue = True
    for symbol in math_operations:
        print(symbol)
    while shouldcontinue:
        operation_symbol = input(f' pick a math operation: ')
        n2 = float(input(f'what\'s your next number?: '))
        calculation_function = math_operations[operation_symbol]
        answer = calculation_function(n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")
        if input(f'Type \'y\' to continue calculation with {answer} or \'n\' to exit.:') == 'y':
            n1 = answer
        else: 
            shouldcontinue = False
calculator()
