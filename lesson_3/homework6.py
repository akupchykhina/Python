# #1) Write a program/function that prints list entities one by one. As an input use a list.
# 	e.g. print_entities(["a", "b", "c"]) should return:
# 		"a"
# 		"b"
# 		"c"


# def print_function(lst):
#     for i in lst:
#         print(i)
#
#
# lst = [1, 5, 6, True]
# print_function(lst)
# print('--------------------------')
# #    2) Write a program/function that converts strings into tuples.
# # 	e.g. convert("abide") should return tuple like:
# # 		("a", "b", "i", "d", "e")


def convert_function(t):
    my_tuple = tuple(t)
    return my_tuple


t = input('Enter any string: ')
print(convert_function(t))
print('--------------------------')

#    3) Write a program/function that removes duplicates and returns only unique values as a list.
# 	e.g. remove_dups("abcdadab") should return ["a", "d", "c", "b"]. Note, order of elements in the list is not important!


# def remove_function(s):
#     s1 = []
#     for i in s:
#         if i not in s1:
#             s1.append(i)
#     print(s1)
#
#
# s = [1, 5, 9, 1, 5, 6, 7, 5]
# remove_function(s)
# print('--------------------------')

def remove_dups(text):
    return list(set(text))

print(remove_dups("absdefadsatbf"))
print('--------------------------')
#    4) Write a program/function that collects certain data as parameters and returns a dictionary object.
# 	e.g. client("John", "Doe", "01/23/1934", "Male", "San Antonio", "TX", "78261") should return a dictionary object like:
# 		{
# 			"Name": "John",
# 			"Lastname": "Doe",
# 			"DOB": "01/23/1934",
# 			"Sex": "Male",
# 			"City": "San Antonio",
# 			"State": "TX",
# 			"ZipCode": "78261"
# 		}


def new_dictionary(x, y):
    my_dictionary = {x: y}
    return my_dictionary


print(new_dictionary('Name', 'John'))

my_dict = {}
my_dict['Name'] = 'Jonh'
my_dict['Lastname'] = 'Doe'
my_dict['DOB'] = '01/23/1958'
my_dict['Sex'] = 'Male'
my_dict['City'] = 'Dallas'
my_dict['State'] = 'TX'
my_dict['ZipCode'] = '75015'

print(my_dict)

print('----------------------------------------------------')

lst = [("Name", "John"), ("Lastname", "Doe"), ("DOB", "01/23/1934"),
       ("Sex", "Male"), ("City", "San Antonio"), ("State", "TX"), ("ZipCode", "78261")]

new_dict = {}
for l in lst:
    new_dict[l[0]] = l[1]
print(new_dict)

print('----------------------------------------------------')

client = ("John", "Doe", "01/23/1934", "Male", "San Antonio", "TX", "78261")

dict_client = {}
dict_client['Name'] = client[0]
dict_client['Lastname'] = client[1]
dict_client['DOB'] = client[2]
dict_client['Sex'] = client[3]
dict_client['City'] = client[4]
dict_client['State'] = client[5]
dict_client['ZipCode'] = client[6]

print(dict_client)

print('-------------------------3---------------------------')


def client_dict(name, last_name, dob, sex, city, state, zip_code):
    client1 = {
        "Name": name,
        "Lastname": last_name,
        "DOB": dob,
        "Sex": sex,
        "City": city,
        "State": state,
        "ZipCode": zip_code
    }
    return client1


print(client_dict("John", "Doe", "01/23/1934", "Male", "San Antonio", "TX", "78261"))