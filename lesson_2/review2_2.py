text = "test"
for i in range(len(text)):
    print(i, text[i])

for k in text:
    print(k)

a = list(range(6))
print(a)

b = list(range(-6, 2))
print(b)

c = list(range(-6, 2, 3))
print(c)

name = "Tonya"
age = 15
msg = "My name is %s and my age is %s" % (name, age)
print(msg)

msg1 = 'My name is {} and my age is {}'
print(msg1.format(name, age))

msg2 = f'My name is {name} and my age is {age}'
print(msg2)
