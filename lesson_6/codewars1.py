import string
import re


def count(str):
    d = {}
    for s in str:
       d[s] = str.count(s)
    return d

print(count("stress"))


def clean_string(s):
    s = s.replace("#", "")
    return s

print(clean_string("sff#nk##j"))


def valid_phone_number(phone_number):
    pattern = r"\(\d{3}\) \d{3}-\d{4}"
    phone_re = re.compile(pattern)
    if phone_re.findall(phone_number):
        return True
    else:
        return False
print(valid_phone_number("(638) 210-7795"))

def validPhoneNumber1(phoneNumber):
    import re
    return bool(re.match(r"^(\([0-9]+\))? [0-9]+-[0-9]+$", phoneNumber))
print(validPhoneNumber1("(638] 210-7799"))

def encode(st):
    d = {"a": "1", "e": "2", "i": "3", "o": "4", "u": "5"}
    for i in st:
        if i in d:
            st = st.replace(i, d[i])

    return st

print(encode('This is an encoding test.'))

def decode(st):
    d = {"1": "a", "2": "e", "3": "i", "4": "o", "5": "u"}
    for i in st:
        if i in d:
            st = st.replace(i, d[i])

    return st

print(decode('Th3s 3s 1n 2nc4d3ng t2st.'))



# # Создание регулярного выражения для номеров телефонов
# phoneRegex = re.compile(r'''(
#     (\d{3}|\(\d{3}\))? # территориальный код
#     (\s|-|\.)?         # разделить
#     (\d{3})              # первый 3 цифры
#     (\s|-|\.)          # разделить
#     (\d{4})              # последние 4 цифры
#     (\s*(ext|x|ext.)\s*(\d{2,5}))?  # добавочный номер
#     )''', re.VERBOSE)

def first_non_repeating_letter(str):
    # str = str.lower()
    s = ""
    if len(str) == 0:
        return s
    else:
        for i in range(len(str)):
            if str[i] not in string.ascii_letters and str.count(str[i]) == 1:
                s += str[i]
            else:
                if str.lower().count(str[i]) + str.upper().count(str[i]) == 1:
                    s += str[i]

        return s[:1]


print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'))

def to_weird_case(str):
    str = str.split()
    t = ""

    for s in str:
        s1 = ""
        for i in range(len(s)):
            if i % 2 == 0:
                s1 += s[i].upper()
            else:
                s1 += s[i]
        t += s1 + " "

    return t[:-1]

print(to_weird_case('stress'))

def title_case(title, minor_words=''):

    title = title.lower()
    title = title.split()
    minor_words = minor_words.lower()
    minor_words = minor_words.split()

    for i in range(len(title)):
        if minor_words == "" or title[i] not in minor_words:
            title[i] = title[i].capitalize()
        title[0] = title[0].capitalize()

    return " ".join(title)


print(title_case("First a of in", "an often into"))
print("------------------------------------------")

def solution(roman):
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0


    for r in roman:
        res += d[r]
    return res
print(solution("MDXXIV"))


def scramble(str1, str2):
    s =''
    for i in str2:
        if str2.count(i) <= str1.count(i):
            s += i

    return s == str2


print(scramble('cedewaraaossoqqyt', 'codewars'))


from urllib.parse import urlparse

def domain_name(url):
    pass


print(domain_name("www.xakep.ru"))

from urllib.parse import urlparse

url = 'www.xakep.ru'
_url = urlparse(url)
hostname = _url.hostname
port = _url.port

print(hostname)


url = "https://www.google.co.in"
img_url = urlparse(url).hostname
print(img_url)

print("-------------------------")


def encrypt_this(text):
    text = text.split()
    res =[]
    for i in text:
        if len(i) < 3:
            res.append(str(ord(i[0])) + i[1:])
        else:
            res.append(str(ord(i[0])) + i[-1] + i[2:-1] + i[1])

    return " ".join(res)

print(encrypt_this("The more he saw the less he spoke"))
print("--------------------------")

def abbreviate(s):
    res = []
    if "-" in s:
        s = s.replace("-", " ")
        s = s.split()
        for i in s:
            if len(i) < 4:
                res.append(i)
            else:
                res.append(i[0] + str(len(i) - 2) + i[-1])
        return "-".join(res)
    else:
        s = s.split(" ")
        for i in s:
            if len(i) < 4:
                res.append(i)
            else:
                res.append(i[0] + str(len(i)-2) + i[-1])
        return " ".join(res)


print(abbreviate("elephant,rid-balbes"))
print("----------------------------")


def group_by_commas(n):
    n = str(n)
    if len(n) < 4:
        return str(n)
    elif len(n) == 4:
        return n[0] + "," + n[1:]
    elif len(n) == 5:
        return n[:2] + "," + n[2:]
    elif len(n) == 6:
        return n[:3] + "," + n[3:]
    elif len(n) == 7:
        return n[0] + "," + n[1:4] + "," + n[4:]
    elif len(n) == 8:
        return n[:2] + "," + n[2:5] + "," + n[5:]
    elif len(n) == 9:
        return n[:3] + "," + n[3:6] + "," + n[6:]
    elif len(n) == 10:
        return n[0] + "," + n[1:4] + "," +n[4:7] + "," + n[7:]

print(group_by_commas(1100100100))

def group_by_commas1(n):
    return format(n,',')

print(group_by_commas1(1100100100))
print("----------------------------")

def format_duration(seconds):
    year = seconds // (360 * 24 * 365)
    day = (seconds % (360 * 24 * 365)) // (24 * 360)
    hour = ((seconds % (360 * 24 * 365)) % (360 * 24)) // 360
    min = (((seconds % (360 * 24 * 365)) % (360 * 24)) % 360) // 60
    sec = (((seconds % (360 * 24 * 365)) % (360 * 24)) % 360) % 60

    return f"{year} years, {day} days, {hour} hours, {min} mins, {sec} seconds"


print(format_duration(17295))
print("----------------------------")


def clean_string(s):
    s = s.split()
    for i in range(len(s)):
        if s[i] == "#":
            s = s.remove(s[i-1])
            return s

    # for i in range(len(s)):
    #     if s[i] == "#":
    #         s = s[:(i-1)] + s[i+1:]

print(clean_string('abc####d##c#'))
print("------------------------")


def domain_name(url):
    x = url.split("/")
    if x[0] == "https:" or x[0] == "http:":
        x = x[2].split(".")
    else:
        x = x[0].split(".")

    if len(x) == 2:
        domain = x[0]
    else:
        domain = x[1]
    return domain


print(domain_name("www.xakep.ru"))

print("--------------------------")

"""
ImportError: an import fails;
IndexError: a list is indexed with an out-of-range number;
NameError: an unknown variable is used;
SyntaxError: the code can't be parsed properly;
TypeError: a function is called on a value of an inappropriate type;
ValueError: a function is called on a value of the correct type, but with an inappropriate value."""

"""Exception Handling


An ATM machine takes the amount to be withdrawn as input and calls the corresponding withdrawal method.
In case the input is not a number, the machine should output "Please enter a number".
Use exception handling to take a number as input, call the withdraw() method with the input as its argument,
and output "Please enter a number", in case the input is not a number.
A ValueError is raised when you try to convert a non-integer to an integer using int()."""


# def withdraw(amount):
#    print(str(amount) + " withdrawn!")
#
# amount = input()
# try:
#     int(amount)
#     withdraw(amount)
# except ValueError:
#     print("Please enter a number")

# menu = ['Fries', 'Sandwich', 'Cheeseburger', 'Coffee', 'Soda']
#
# i = input()
# try:
#     print(menu[int(i)])
# except:
#     print("Item not found")
# else:
#     print("Thanks for your order")

try:
  print(1)
  print(1 + "1" == 2)
  print(2)
except TypeError:
  print(3)
else:
  print(4)

# tweet = input()
#
# try:
#     if len(tweet) <43:
#         print(tweet)
#     else:
#         raise ValueError
# except:
#     print("Error")
# else:
#     print("Posted")
print("-------------")
"""You are given a books.txt file, which includes book titles, each on a separate line.
Create a program to output how many words each title contains, in the following format:
Line 1: 3 words
Line 2: 5 words
...

Make sure to match the above mentioned format in the output.
To count the number of words in a given string, you can use the split() function, or,
alternatively, count the number of spaces (for example, if a string contains 2 spaces,
then it contains 3 words)."""

with open("books.txt") as f:
   lines = f.readlines()
   for i in range(len(lines)):
       s = lines[i].count(" ")
       print(f"Line {i+1}: {s} words")


file = open("books.txt", "r")
titles = file.readlines()
for title in titles:
    title = title.split(" ")
    res = ""
    for i in range(len(title)):
        res += title[i][0]
    print(res)

#your code goes here

file.close()




