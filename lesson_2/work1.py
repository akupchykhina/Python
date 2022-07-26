a = [2, 200, 3, 19, 56, 59, 75, 77, 56, 88, 139, 200, 18, 19, 15, 221]

for i in a:
    if i % 2 == 1:
        print(i)
        if i == 139:
            break

b = list(range(18, 0, -4))
print(b)

list1 = []
for x in range(18, 0, -4):
    list1.append(x)
print(list1)
