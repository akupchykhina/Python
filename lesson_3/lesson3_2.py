list1 = ['test 1', 'test 5', 'test 11', 'test 19']

print(list1)
list1[1] = True
list1.append(15)
print(list1)

my_tuple = (15, True, 'test1') #кортеж - в отличие от лсита - нельзя изменить
print(my_tuple)

my_dictionary = {
    "name": "Bob",
    "last_name": "Pop",
    "DOB": "2000-03-21"
}

print(my_dictionary)
my_dictionary["name"] = "POl"
print(my_dictionary)

my_set = {"element1", "element2", "el3", "el4", "el3"}

print(my_set)
print(len(my_set))
