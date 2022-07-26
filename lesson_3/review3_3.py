# def function_name(x):
#     return f"Hello, {x}"
#
#
# y = input('What is your name? ')
# print(function_name(y))

my_list = [12, "Tonya", True]
print(my_list)
my_list.append("Hello")
print(my_list)
my_list.pop() #удаляет последний элемент из списка
print(my_list)
my_list.pop(1)
print(my_list)
my_list.insert(1, 56)
print(my_list)
my_list.insert(0, [1, 2, 2])
print(my_list)
my_list.append(("toni", "boni"))
print(my_list)
my_list.insert(-1, "APPLE") #-1 указывает что хотим вставить новый элемент вторым с конца. Если хотим последним - используем pop
print(my_list)

print(my_list[-1]) #вывести последний элемент списка
print(my_list[2])

my_list1 = [1, 2, 5, 99, 15, 1, 16]
print(my_list1)
print(set(my_list1))

print(len(my_list1) == len(set(my_list1))) #сравниваем длину листа и сета, чтобы понять, есть ли в листе одинаковые элементы

print('------------------------------------')

my_dict = {
    'book':'Tom Soyer',
    'Author': 'Mark Twen',
    'year': 2022,
    'new': True,
    1: 'yes'
}

print(my_dict)

my_dict['year'] = 2020 #обновить значение по ключу
print(my_dict)

my_dict['date'] = 2003 #добавить новы ключ со значением
print(my_dict)

my_dict[(15, 21)] = ['age', 'year']
print(my_dict)

print(my_dict['date'])

my_dict.pop('date')
print(my_dict)

print(my_dict.keys())