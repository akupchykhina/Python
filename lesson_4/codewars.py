# def duplicate_count(text):
#     text = text.upper()
#     d = {}
#     for i in range(len(text)):
#         d[text[i]] = text.count(text[i])
#     return d
#
#
# print(duplicate_count("Hello Welcome How are you"))
import string

import odd as odd


def duplicate_count(text):
    text = text.upper()
    set1 = []
    for i in range(len(text)):
        if text.count(text[i]) >1:
            set1.append(text[i])
    st = set(set1)
    return len(st)


print(duplicate_count("Hello Welcome How are you"))
print("-------------------")


def is_isogram(string):
    string = string.upper()
    for i in range(len(string)):
        if string.count(string[i]) > 1:
            return False
        else:
            return True


print(is_isogram("Welcome"))
print("-------------------")


def iso(s):
    s = s.lower()
    st = set(s)
    return len(st) == len(s)

print(iso("tonya"))
print("-------------------")


def duplicate_encode(word):
    word = word.upper()
    w = ""
    for i in word:
        if word.count(i) == 1:
            i = "("
            w += i
        else:
            i = ")"
            w += i

    return w

print(duplicate_encode("Hello"))
print("-------------------")


def to_jaden_case(string):
    # st = string.split(" ")
    # for i in range(len(st)):
    #     st[i] = st[i].replace(st[i][0], st[i][0].upper())
    #     for s in st:
    #         for j in range(len(s)-1):
    #             s[j+1] = s[j+1].replace(s[j+1], s[j+1].lower())
    return ' '.join([i.capitalize() for i in string.split()])


print(to_jaden_case("welcome delete eyes eyetro"))

def alphabet_position(text):
    text = text.lower()
    alph = string.ascii_lowercase
    text1 = []
    for t in text:
        if t in alph:
            text1.append(t)

    for l in range(len(text1)):
        text1[l] = alph.index(text1[l])+1
        text1[l] = str(text1[l])
    return " ".join(text1)


print(alphabet_position("hello dsf 7hgn5"))
print("-------------------")


contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

# name = input("Enter a contact name, please: ")
# cont = []
# for i in range(len(contacts)):
#     if name in contacts[i]:
#         cont.append(contacts[i])
#         if len(cont) != 0:
#             print(f'{contacts[i][0]} is {contacts[i][1]}')
#         else:
#             print("Not found")


# a = [5, 9, 8, 9, 7]
#
# b = int(input())
#
# for x in [a]:
#     if b in x:
#         print("yes")
#     else:
#         print("no")

skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}

print(list(skills & job_skills)[0])

# word = input()
# # l = []
# # for w in word:
# #     if w not in ('a', 'e', 'i', 'o', 'u'):
# #         l.append(w)
# #
# # print(l)
# l = [i for i in word if i not in ('a', 'e', 'i', 'o', 'u')]
# print(l)

def maskify(cc):
    xx = ''
    if len(cc) < 5:
        return cc
    else:
        for i in range(len(cc)-4):
            xx += "#"
        for k in range(len(cc)-4, len(cc)):
            xx += cc[k]
        return xx
print(maskify("159367895246"))
print(maskify("qwerty"))


def DNA_strand(dna):
    d = []
    for t in dna:
        d.append(t)
    for i in range(len(d)):
        if d[i] == "A":
            d[i] = "T"
        elif d[i] == "T":
            d[i] = "A"
        elif d[i] == "C":
            d[i] = "G"
        elif d[i] == "G":
            d[i] = "C"
        i +=1

    return "".join(d)
print(DNA_strand("ACTAG"))

# другие 2 способа
# замена символов
# pairs = {'A':'T','T':'A','C':'G','G':'C'}
# def DNA_strand(dna):
#     return ''.join([pairs[x] for x in dna])
#
# import string
# def DNA_strand(dna):
#     return dna.translate(string.maketrans("ATCG","TAGC"))

def order(sentence):
    sentence = sentence.split(" ")
    s = {}
    for sent in sentence:
        for i in range(len(sentence)+1):
            if str(i) in sent:
                s[i-1] = sent
            i += 1
    s1 =[]
    for j in range(len(s)):
        s1.insert(j, s[j])

    return " ".join(s1)


print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))

salaries = [2000, 1800, 3100, 4400, 1500]
bonus = 550

def add_bonus(x):
    return x + bonus

print(list(map(add_bonus, salaries)))
print("===========================")

def abbrev_name(name):
    s = []
    for n in name.split(" "):
        s += n[0][0].upper()

    return ".".join(s)
print(abbrev_name("Tonya Kupchyk"))

def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))
print("__________________")


def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for n in range(2, x):
        if x % n == 0:
            return False
    return True


def primeGenerator(a, b):
    for i in range(a, b):
        if isPrime(i):
            yield i

f = 10
t = 20

print(list(primeGenerator(f, t)))

print("========================")
"""ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything
but exactly 4 digits or exactly 6 digits.
If the function is passed a valid PIN string, return true, else return false."""
import string

def validate_pin(pin):
    if len(pin) != 4 and len(pin) != 6:
        return False
    else:
        for i in pin:
            if i in string.digits:
                continue
            else:
                return False
        return True


print(validate_pin("778s64"))

print("------------------------")
'''Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized
(known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"'''

def to_camel_case(text):
    text = text.replace("_", " ")
    text = text.replace("-", " ")
    text = text.split(" ")

    for i in range(1, len(text)):
        text[i] = text[i].capitalize()

    return "".join(text)

print(to_camel_case("the-Apple_is-good"))

print("-------------------")
import string

def is_pangram(s):
    s = s.upper()
    s1 = ''
    for i in range(len(s)):
        if s[i] in string.ascii_uppercase:
            s1 += s[i]
    return len(set(s1)) == len(string.ascii_uppercase)

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))

print("------------------------------")
'''Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the missing
second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']'''

def solution(s):
    s1 = []
    if len(s) % 2 != 0:
        s = s +"_"
    for i in range(0, len(s)-1, 2):
        s1.append(s[i:i+2])

    return s1

print(solution("592dfdg"))



