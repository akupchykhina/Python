# x = 'Kolbasa'
# for i in range(1, 11):
#     print(i, x)
#
# y = "Python"
# for i in range(10):
#     print(i+1, y)
#
# print('----------------------')

# n = int(input('Enter a number: '))
#
# while n < 2:
#     n = int(input('This number is less than 2! Try again: '))
# else:
#     for i in range(n):
#         print('*'*(n-i))

print('----------------------')

m = 100
n = 20
p = 6

for i in range(p):
    m = m + n * m / 100
    i += 1
    print(i, m)

print('----------------------')

print(list(range(0, 100, 10)))

print('----------------------')

m, n = 5, -5

if m < n:
    for i in range(m, n+1, 1):
        print(i)
else:
    for i in range(m, n-1, -1):
        print(i)

print('----------------------')

m, n = 15, 5

for i in range(m, n-1, -1):
    if i % 2 == 1:
        print(i)

print('----------------------')

string = input('Enter a string: ')

while string != 'END':
    print(string)
    string = input('Enter a string: ')

print('----------------------')

string = input('Enter a string: ')

while string != 'END' and string != 'end':
    print(string)
    string = input('Enter a string: ')
