# def sum_function(x, y):
#     print(x + y)
#
#
# sum_function(4, -4)


# def my_function(x, y):
#     z = (x + y) / 2
#     text = f'Result of our calculation: {z}'
#     print(text)
#
#
# x1 = 14
# y1 = 23
# my_function(x1, y1)
#
# my_function(4, 8)
#
# x2 = int(input('Enter a number x: '))
# y2 = int(input('Enter a number y: '))
# my_function(x2, y2)

# def new_function(x, y):
#     result = x * y / 5
#     return result
#
#
# x1 = 15
# y1 = 25
# res = new_function(x1, y1)
# print(f'result = {res}')

x = 45 #это глобальная перменная и к функции отношения не имеет,
# в функции своя локальная переменная х


def function1():
    global x #обращаемся к глобальной переменной х = 45, и работаем с ней
    x = 12
    x += 1
    print(x)


function1()
print(x)
