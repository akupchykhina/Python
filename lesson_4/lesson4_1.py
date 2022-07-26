# file = open("text.txt", "r") # ключ r - читать файл, другие ключи -  a - добавлять, w - писать, x - создавать
#
# # print(file.read())
# # print(file.readline()) #построчно
# # print(file.readline()) #построчно
# # print(file.read(5))
#
# for line in file:
#     print(line)
#
# file.close()

#создание файла
# file = open("test_1.txt", "w")
#
# file.write("Здравствуйте!")
#
# file.close()
#
# file = open("test_1.txt", "r")
#
# print(file.read())
#
# file.close()

#короткий вариант чтения файла и закрытие

with open("test_1.txt", "r") as file:
    print(file.read())

with open("text.txt", "w") as file: #перезаписывает существующий файл
    file.write("What is the weather today?")

with open("text.txt", "r") as file:
    print(file.read())


