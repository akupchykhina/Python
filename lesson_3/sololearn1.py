# total = 0
# price = 100
# lst = [15, 1, 2, 45, 23]
# for i in lst:
#     if i < 3:
#         continue
#     else:
#         total += price
#
# print(total)


def total_price(a, b, c, d, e):
    total = 0
    price = 100
    lst = [a, b, c, d, e]
    for i in lst:
        if i < 3:
            continue
        else:
            total += price

    print(total)

total_price(5, 6, 7, 2, 11)

i = 0
x = 0
while i < 4:
    x+=i
    i+=1

print(x)


weight = float(input())
height = float(input())
BMI = weight / (height * height)
print(BMI)
if BMI < 18.5:
    print('Underweight')
if 18.5 <= BMI < 25:
    print('Normal')
if 25 <= BMI < 30:
    print('Overweight')
if BMI >= 30:
    print('Obesity')
