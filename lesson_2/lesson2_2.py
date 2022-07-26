for x in range(6):
    print(x)

for y in range(0, 10, 2):
    print(y)

print("while")

i = 1

while i < 6:
    print(i)
    i += 5

print("next")

j = 1

while j < 600:
    print(j)
    if j == 10:
        break
    j += 1

print("next")

k = 0

while k < 20:
    k += 1
    if k == 10:
        continue
    print(k)
    print(f'test {k}')

