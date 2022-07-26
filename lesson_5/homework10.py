# #   1) Write a function to compare 2 numbers.
# 	E.g. compare(2, 3) should return False otherwise should return True.
def compare_function(x, y):
    if x < y:
        return True
    else:
        return False


# print(compare_function(2, 3))
# print('-----------------------------')
#     2) Modify the previous function to compare only positive numbers.
# 	In case of negative numbers it will return a print statement like: "Can compare only positive numbers!".

#
def pos_compare_function(x, y):
    if x < 0 or y < 0:
        text = "Can compare only positive numbers!"
        return text
    else:
        if x < y:
            return True
        else:
            return False
#
#
# print(pos_compare_function(-7, -33))
# print('-----------------------------')
# #     3) Write a function to sum 2 numbers.
# # 	E.g. add(4, 5) should return 9 as a result.


def sum_function(x, y):
    result = x + y
    return result
#
#
# print(sum_function(5, 6))
#
# print('-----------------------------')
# #     4) Write a function to subtract 2 numbers.
# # 	E.g. sub(4, 2) should return 2 as a result.
#
#
# def sub_function(x, y):
#     result = x - y
#     return result
#
#
# print(sub_function(5, 6))
#
# print('-----------------------------')
# #     5) Write a function that returns a type of input.
# # 	E.g. give_a_type("test") should return a print statement like: "string".
#
#
# def type_function(x):
#     return type(x)
#
#
# x = input("Enter something: ")
# print(type_function(x))
# print('-----------------------------')
#
#
# def type_function(z):
#     return type(z)
#
#
# z = True
# print(type_function(z))
# print('-----------------------------')
#
# def type_function1(y):
#     if type(y) == str:
#         return 'string'
#
#
# y = input("Enter something: ")
# print(type_function1(y))
# print('-----------------------------')
#
#
# def get_type(t):
#     if isinstance(t, str):
#         return "string"
#     if isinstance(t, int):
#         return "integer"
#     return "unknown"
#
#
# t = input("Enter any text: ")
# print(get_type(t))
# print('-----------------------------')
# #     6) Write a function that prints input vertically.
# # 	E.g. print_vertical("test me please") should return:
# # 		t
# # 		e
# # 		s
# # 		t
# #
# # 		m
# # 		e
# #
# # 		p
# # 		l
# # 		e
# # 		a
# # 		s
# # 		e
#
#
# def vertical_function(z):
#     for i in z:
#         print(i)
#
#
# z = input('Enter a string: ')
# vertical_function(z)
# print('-----------------------------')
#
# #     7) Write a function that concatenates 2 strings.
# # 	E.g. concat("abc" , "123") should return a print statement like: "adc123".


def concat_function(a, b):
    result = a + b
    return result

#
#
# a, b = 'tonya', 'python'
# print(concat_function(a, b))
#
#
# def concat(text_1, text_2):
#     return text_1 + text_2
#
#
# print(concat("tonya", "python"))


def reverse(x):
    if not isinstance(x, str):
        raise TypeError
    return x[::-1]
