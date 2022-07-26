# password = input('Enter your password: ')
# password1 = input('Confirm your password: ')
#
# if password == password1:
#     print('Accepted')
# else:
#     print('Declined')

# num = input('Enter a number: ')
#
# while not num.isdigit():
#     num = input('It is not a number!!! Try again: ')
# else:
#     num = int(num)
#
# if num % 2 == 0:
#     print("this number is even")
# else:
#     print("this number is odd")
#
# #2
# name = input('Enter your name: ')
# age = int(input(f'{name}, enter your age: '))
#
# if age < 18:
#     print('Access denied!')
# else:
#     print('Access granted')

#3

# weight = float(input('Enter your weight: '))
# height = float(input('Enter your height: '))
#
# BMI = weight / height ** 2
#
# if 18.5 <= BMI <= 25:
#     print(f'BMI={BMI}. Your weight is optimal')
# elif BMI > 25:
#     print(f'BMI={BMI}. Overweight')
# else:
#     print(f'BMI={BMI}. Underweight')

#4

# x = int(input('Enter a number: '))
#
# if -1 < x < 17:
#     print(f'{x} belongs to this range')
# else:
#     print(f'{x} doesn\'t belong to this range')

#5
#
# y = int(input('Enter a number: '))
#
# if y in range(-29, -1) or y in range(8, 26):
#     print(f'{y} is in the range')
# else:
#     print(f'{y} is not in the range')

#6
# a = int(input())
# b = int(input())
# c = int(input())
#
# while a <= 0 or b <= 0 or c <= 0:
#     print('One or more numbers is negative')
#     break
# else:
#     if a + b <= c or a + c <= b or b + c <= a:
#         print('can not create a triangle - one side is more than sum of other sids')
#     else:
#         print(f'The triangle exists')

#7
"""
Write a program that takes three positive numbers and determines the type of triangle whose side lengths are equal to the given numbers.
The program should display text on the screen - a kind of triangle ("Equilateral", "Isosceles" or "Scales").
"""
# a = abs(int(input())) - конвертирует отрицательные числа в положительные
# a = int(input())
# b = int(input())
# c = int(input())
#
# while a <= 0 or b <= 0 or c <= 0:
#     print('One or more numbers is negative')
#     break
# else:
#     if a + b <= c or a + c <= b or b + c <= a:
#         print('can not create a triangle - one side is more than sum of other sids')
#     else:
#         if a == b == c:
#             print('this triangle is Equilateral')
#         elif a == b or a == c or b == c:
#             print('this triangle is Isosceles')
#         else:
#             print('this triangle is Scales')

#8
'''
Write a program where the function more_than_five(lst) receives a list of integers.
The result of the function should be a new list, which contains only those numbers that are greater than 5 modulo.
'''

# lst = [8, 2, 5, 9, -8]
# print(lst)
# lst[0] = 10
# print(lst)

def more_than_five(lst):
    new_list = []
    for i in lst:
        if abs(i) > 5:
            new_list.append(abs(i))
    #print(new_list)
    return new_list

print(more_than_five([-5, 48, -1, 0, 5, -10, 7, -15]))
