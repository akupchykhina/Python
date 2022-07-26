"""
7.1 Create a program/function that gets a parameter as a text,
    creates file "text.txt" and inserts the text into the file.
    As the result of the program/function, we have to get our file "text.txt"
    with the content from the parameter.
"""

#
# def file_function(text):
#
#     with open("text1.txt", "w") as file:
#         file.write(text)
#
#     with open("text1.txt", "r") as file:
#         print(file.read())
#
#
# file_function("Hello! My name is Tonya")

"""
7.2 Create a program/function that gets 2 parameters,
    first parameter a file name,
    second parameter character (letter, number) 
    and replaces all characters in the file to 0 which equals the second parameter.
    E.g. we have a file "my_text.txt" with the text "Hello Python! Lesson 7",
    we pass the second parameter as "e" to the program/function, and as the result
    text in the file will be "H0llo Python! L0sson7" 
"""

letter = "o"
file_name = "text1.txt"
with open(file_name) as file:
    line = file.readline()
    print(line)

    for l in line:
        if l == letter:
            line = line.replace(l, '0')
    print(line)


    with open(file_name, "w") as file:
        file.write(str(line))

#
# str1 = "Hello! My name is Tonya"
#
# for s in str1:
#     if s == "o":
#         str1 = str1.replace('o', '0')
# print(str1)




