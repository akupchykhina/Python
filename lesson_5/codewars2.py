import string


def in_array(array1, array2):
    r = []
    for i in array1:
        for j in array2:
            if i in j:
                r.append(i)
    return sorted(list(set(r)))


a1 = ["arp", "mice", "bull"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1, a2))
print("++++++++++++++++++++++++++++++++++++")

# s=[]
# def expanded_form(num):
#     if num ==0:
#         return s
#     l = num % 10
#     s.append(l)
#     expanded_form(num // 10)
#
# expanded_form(45621)
# print(s)

def expanded_form(num):
    x = [int(a) for a in str(num)]
    s = []
    n = len(x)
    for i in range(n):
        if x[i] != 0:
            s.append(str(x[i]*(10**(n-i-1))))
    return " + ".join(s)


print(expanded_form(40506))
print("---------------------------")


# class Shape:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         print(self.width * self.height)
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         super(Rectangle, self).__init__(width, height)
#
#     def perimeter(self, width, height):
#         print(2 * (self.width + self.height))
#     # your code goes here
#
#
# w = int(input())
# h = int(input())
#
# r = Rectangle(w, h)
# r.area()
# r.perimeter(w, h)

print("----------------------------")

def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]


print(feast("great blue heron", "garlic naap"))
print("----------------------------")

def solution(s):
    for i in s:
        if i in string.ascii_uppercase:
            s = s.replace(i, " "+i)
    s = s.split(" ")
    for i in s:
        if i == "":
            s.remove(i)
    return " ".join(s)

print(solution("breakCamel"))
print("----------------------------")

def wave(people):
    s = []
    for i in range(len(people)):
        if people[i] == " ":
            continue
        p = people[:i] + people[i].upper() + people[i + 1:]
        # p = people.replace(people[i], people[i].upper())
        s.append(p)
    return s


print(wave("people hello"))
print("----------------------------")

def two_sort(array):
    a = sorted(array)
    return "***".join(a[0])

print(two_sort(["take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]))
print("----------------------------")


def format_duration(seconds):

    year = seconds // (360 * 24 * 365)
    day = (seconds % (360 * 24 * 365)) // (24 * 360)
    hour = ((seconds % (360 * 24 * 365)) % (360 * 24)) // 360
    min = (((seconds % (360 * 24 * 365)) % (360 * 24)) % 360) // 60
    sec = (((seconds % (360 * 24 * 365)) % (360 * 24)) % 360) % 60


    return f"{year} years, {day} days, {hour} hours, {min} mins, {sec} seconds"

print(format_duration(17295))
print("---------------------")

def camel_case(str):
    str = str.split(" ")
    for i in range(len(str)):
        str[i] = str[i].capitalize()

    return ''.join(str)

print(camel_case("hello python my name is tonya"))
print("---------------------")

def diamond(n):
    s = ""
    if n > 0 and n % 2 == 1:
        for i in range(1, n+1, 2):
            s += " "*int((n - i)/2) + "*"*i +"\n"
        for i in range(n-2, 0, -2):
            s += " " * int((n - i) / 2) + "*" * i + "\n"
        return s


print(diamond(11))
# "  *\n ***\n*****\n ***\n  *\n"
print("---------------------")
def is_anagram(test, original):
    return sorted(test.upper()) == sorted(original.upper())

print(is_anagram("Buckethead", "DeathCubeK"))
print("---------------------")
def capitals(word):
    l = []
    for i in range(len(word)):
        if word[i] in string.ascii_uppercase:
            l.append(i)
    return l

print(capitals("HellO"))
print("---------------------")

def remove_url_anchor(url):
    for u in url:
        if u == "#":
            i = url.index(u)
            url = url[:i]
    return url

print(remove_url_anchor("www.codewars.com"))
print("----------------------------------")


def generate_hashtag(s):
    if s == "":
        return False
    else:
        s = s.split(" ")
        for i in range(len(s)):
            s[i] = s[i].capitalize()
        s.insert(0, "#")
        s1 = "".join(s)
        if len(s1) > 140:
            return False
        else:
            return s1


print(generate_hashtag("hello my name is tonya"))
print("----------------------------------")

def first_non_repeating_letter(str):
    str = str.lower()
    s = ""
    if len(str) == 0:
        return s
    else:
        for i in range(len(str)):
            if str.count(str[i]) == 1:
                s += str[i]

        return s[:1]

print(first_non_repeating_letter("Go hang a salami, I\'m a lasagna hog!"))
print("----------------------------------")

def a(n):
    for i in range(1, n):
        return i

print(a(5))
print("-----------------------------")

def to_weird_case(str):
    str = str.split(" ")
    for j in range(len(str)):
        for i in range(len(str[j])):
            t = ""
            if i % 2 == 0:
                str[j] = str[j].replace(str[j][i], str[j][i].upper())

    return " ".join(str)

print(to_weird_case('Weird string test case'))
print("-----------------------------")

def better_than_average(class_points, your_points):
    number_of_students = len(class_points)
    sum_class_points = 0
    for i in class_points:
        sum_class_points += i

    average_points = sum_class_points / number_of_students

    return your_points > average_points

print(better_than_average([59, 68, 99, 78, 56, 48, 78, 85, 95, 64, 75], 88))

def even_chars(st):
    if len(st) <2 or len(st) > 100:
        return "invalid string"
    else:
        s = []
        for i in range(0, len(st)-1, 2):
            s.append(st[i+1])
        return s

print(even_chars("a"))

def solution(full_text, search_text):
    return full_text.count(search_text)

print(solution("abbabbbvvvvbbb", "bbb"))


def we_rate_dogs(str, rating):
    str = str.split(" ")
    for i in range(len(str)):
         if "/10" in str[i]:
             str[i] = f"{rating}/10"
    return " ".join(str)
print(we_rate_dogs("This is Tucker. He would like a hug. 3/10 someone hug him", 11))
print("---------------------------")

def pyramid(n):
    s = ""
    if n > 0:
        for i in range(1, n):
            s += " " * int(n - i) + "/" + " "*((i-1)*2) + "\\" + "\n"
        for i in range(n, n+1):
            s += "/" + "_"* (n*2 -2) + "\\" + "\n"

        return s
print(pyramid(8))

def diamond(n):
    s = ""
    if n > 0 and n % 2 == 1:
        for i in range(1, n+1, 2):
            s += " "*int((n - i)/2) + "*"*i +"\n"
        for i in range(n-2, 0, -2):
            s += " " * int((n - i) / 2) + "*" * i + "\n"
        return s


print(diamond(11))
print("-----------------------")


def remove_duplicate_words(s):
    s = s.split(" ")
    res = []
    for i in s:
        if i not in res:
            res.append(i)
    return " ".join(res)

print(remove_duplicate_words('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))


def capitalize(s):
    t = []
    for i in s:
        t.append(i)
    for j in range(0, len(t), 2):
        t[j] = t[j].upper()
    res1 = "".join(t)
    h = []
    for i in s:
        h.append(i)
    for j in range(1, len(h), 2):
        h[j] = h[j].upper()
    res2 = "".join(h)
    res = []
    res.append(res1)
    res.append(res2)
    return res
print(capitalize("helloeverybody"))