# Напишите программу, которая считает стоимость трех компьютеров, состоящих из монитора,
# системного блока, клавиатуры и мыши.
# На вход программе подаётся четыре целых числа, каждое на отдельной строке. В первой строке — стоимость монитора,
# во второй строке — стоимость системного блока,
# в третьей строке — стоимость клавиатуры и в четвертой строке — стоимость мыши.
import math

monitor = int(input("Введите стоимость монитора: "))
block = int(input("Введите стоимость системного блока: "))
klava = int(input("Введите стоимость клавиатуры: "))
mouse = int(input("Введите стоимость компьютерной мыши: "))
total = (monitor + block + klava + mouse) * 3
print(total)

# Напишите программу, в которой вычисляется сумма, разность и произведение двух целых чисел, введенных с клавиатуры.

a, b = int(input()), int(input())
print(a+b)
print(a-b)
print(a*b)

# Напишите программу, которая считывает целое положительное число xx и выводит на экран последовательность
# чисел x, \, 2x, \, 3x,\,4xx,2x,3x,4x и 5x5x, разделённых тремя черточками.

x = int(input("ВВедите целое положительное число x: "))
print("Последовательность чисел: ")
print(x, 2*x, 3*x, 4*x, 5*x, sep='---')

# Напишите программу, которая находит полное число метров по заданному числу сантиметров.
c = int(input("Введите число c: "))
print(f"{c} см = {c/100} м")


#Безумный титан Танос собрал все 6 камней бесконечности и намеревается уничтожить половину населения Вселенной
# по #щелчку пальцев. При этом если население Вселенной является нечетным числом,
# то титан проявит милосердие и округлит #количество выживших в большую сторону.
# Помогите Мстителям подсчитать количество выживших.

population = int(input("Введите количество населения Вселенной: "))
print(f'Population = {population} millions')
if population % 2 == 1:
    new_population = math.ceil(population / 2)
else:
    new_population = population / 2
print(new_population)

population1 = int(input())
survivors = population1 // 2 + population1 % 2
print(survivors)