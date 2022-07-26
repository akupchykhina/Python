import abc
from string import ascii_lowercase

word = "Hello python!"
for b in word:
    print(b)

print("next")

# 1) Write a program that uses loop and prints numbers from 1 to 100
# but the program should stop if a number is equal to 45.

i = 0

while i < 101:
    i += 1
    print(i)
    if i == 45:
        break
print("even")

# 1) Write a program that prints even numbers from 1 to 20.

j = 0

while True:
    j += 1
    if j % 2 == 0:
        print(j)
        if j == 20:
            break

print("next")

#   2) Write a program that prints odd numbers from 1 to 30.

for a in range(1, 30, 2):
    print(a)

print("odd")

z = 0
while z < 30:
    z += 1
    if z % 2 == 1:
        print(z)
print("next")
#  1) Write a program that prints numbers from 30 to 0 in decreasing order.

k = 31

while k > 0:
    k -= 1
    print(k)

print("next")

a = str(ascii_lowercase)
print(a)

i = 1
while i < 11:
    print(i, a[i-1])
    i += 1