apple = 20
while apple >= 10:
    print(apple, "apple")
    apple -= 2

x = "world"
for i in x:
    print(i)

lst = ["hello", 'Bob', 'How', 'are', 'you?', 'today']
for k in lst:
    if k == "Bob":
        continue
    print(k)
    if k == "you?":
        break

a = int(input("Enter integer a:"))
b = int(input("Enter integer b:"))

if a > b:
    print("a is more than b")
elif a == b:
    print("a = b")
else:
    print("a is less than b")