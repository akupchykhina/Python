a = 6
b = 5


if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

x, y, z = 5, 2, 8

if (x > y) and (z > x):
    print("true")

m, n, l = 1, 2, 3

if m > n or l > m:
    print("true")

if m != n:
    if l > m:
        print("true")