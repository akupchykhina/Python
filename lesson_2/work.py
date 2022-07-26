from string import ascii_letters, ascii_uppercase, ascii_lowercase

a = str(ascii_lowercase)
print(a)

i = 1
while i < 11:
    print(i, a[i-1])
    i += 1

#второй способ
for k in range(5):
    print(k, a[k-1])

#ввести секуды, вывксти чвсы, минуты и секунды

sec = int(input("Enter number of seconds: "))
h = sec // 3600
m = sec % 3600 // 60
s = sec % 3600 % 60
print(f"{sec} seconds = {h} h {m} m {s} s")
