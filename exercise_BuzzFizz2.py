rangehundred = range(1,101)

for n in rangehundred:
    if (n % 3 == 0) and (n % 5 == 0):
        print(f'FizzBuzz')     
    elif n % 5 == 0:
        print(f'Buzz')
    elif n % 3 == 0:
        print(f'Fizz')
    else:
        print(n)