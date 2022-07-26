a = input('Enter a number: ')
while not a.isdigit():
    a = input('It is not a number! Try again: ')
else:
    a = int(a)

c = input('Enter an operation: ')
while c not in ['+', '-', '*', '/']:
    c = input('This operation not defined!!! Try again: ')
else:
    b = input('Enter one more number: ')
    while not b.isdigit():
        b = input('It is not a number! Try again: ')
    else:
        b = int(b)

    if c == '+':
        print(a + b)
    elif c == '-':
        print(a - b)
    elif c == '*':
        print(a * b)
    elif c == '/':
        if b == 0:
            print('Division by zero')
        else:
            if a % b == 0:
                print(int(a / b))
            else:
                print(a/b)
    else:
        print('This operation not defined')
