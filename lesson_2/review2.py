#name = input()
#print(f'Hello, {name}')

#a = input("What is your name?: ")
#print(f"How are you, {a}?")

#print("-----------")

#x = int(input("Enter x: "))
#y = int(input())
#print(x + y)

# Напишите программу, которая считывает три целых числа и выводит на экран их сумму.
# Kаждое число записано в отдельной строке.

x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

print(f"x+y+z= {x + y + z}")

# Напишите программу, вычисляющую объём куба и площадь его полной поверхности, по введённому значению длины ребра.
# На вход программе подается одно целое число – длина ребра.
# Примечание. Объём куба и площадь полной поверхности можно вычислить по формулам V = a^3,  S = 6a^2

a = int(input("Enter cube side: "))
print(f"Volume V = {a**3}")
print(f"Square S = {6*(a**2)}")

# Напишите программу вычисления значения функции
# f(a, \, b) = 3(a + b)^3 + 275b^2 - 127a - 41 по введеным целым значениям aa и bb.

b, c = int(input("Enter b: ")), int(input("Enter c: "))
f = 3 * (b + c) ** 3 + 275 * c ** 2 - 127*b - 41
print(f"f = {f}")

# Напишите программу, которая считывает целое число,
# после чего на экран выводится следующее и предыдущее целое число с пояснительным текстом.

i = int(input("Введите целое число i: "))
j = i + 1
k = i - 1
print(f"Следующее число: {j}")
print(f"Предыдующее число: {k}")


