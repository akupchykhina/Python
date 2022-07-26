def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)


# print(power(2, 4))
#
# nums = [1, 2, 8, 3, 7]
#
# res = list(filter(lambda x: x%2==0, nums))
#
# print(res)
#
# def func(**kwargs):
#   print(kwargs["zero"])
#
# func(a = 0, zero = 8)
#
#
def spell(txt):
    if len(txt) == 0:
        return txt
    else:
        return spell(txt[1:]) + txt[0]


# txt = input()
# spell(txt)
# for i in spell(txt):
#     print(i)