import datetime
import string

print(datetime.date.today())
"""Move the first letter of each word to the end of it,
then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !"""

def pig_it(text):
    text = text.split(" ")
    for i in range(len(text)):
        if text[i] in string.punctuation:
            continue
        else:
            text[i] = text[i] + text[i][0] + "ay"
            text[i] = text[i][1:]

    return " ".join(text)


print(pig_it("Hello My name is Python !"))

"""Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false"""

def solution(string, ending):
    t = len(string)
    l = len(ending)
    if string[t-l:] == ending:
        return True
    else:
        return False

def solution1(string, ending):
    return string.endswith(ending)

print(solution("string", "rang"))
print(solution1("string", "rang"))

s = "string"
print(s[2:])
print("-----------------------------")

'''Given an array (arr) as an argument complete the function
countSmileys that should return the total number of smiling faces.

Rules for a smiling face:

Each smiley face must contain a valid pair of eyes.
Eyes can be marked as : or ;
A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
Every smiling face must have a smiling mouth that should be marked with either ) or D
No additional characters are allowed except for those mentioned.

Valid smiley face examples: ":)", ";)", ':D', ';D', ';-D', ':-D', ':~D', ':~D', ':~)', ';~)', ':-)', ';-)'
Invalid smiley faces: ;( :> :} :]

Example
countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
Note
In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same.

'''

def count_smileys(arr):
    count = 0
    for i in range(len(arr)):
        if ")" in arr[i] or "D" in arr[i]:
            count += 1
    return count

print(count_smileys([':)',':(',':D',':O',':;']))
print("--------------------------")

def reverse_words(s):
    s = s.split(" ")
    s1 = []
    for i in range(len(s), 0, -1):
        s1.append(s[i-1])
    return " ".join(s1)

print(reverse_words("Hello My name is Python"))
print("------------------------------")


def tower_builder(n_floors):
    t = []
    s = ""
    for i in range(0, n_floors):
        s = ' '*(n_floors-i-1) + "*"*(i*2+1) + ' '*(n_floors-i-1)
        t.append(s)
    return t


print(tower_builder(3))


def anagrams(word, words):
    res = []
    for i in range(len(words)):
        if sorted(word) == sorted(words[i]):
            res.append(words[i])
    return res


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print("===================")

def decor(func):
    def wrap(*args, **kwargs):
        print("***")
        func(*args, **kwargs)
        print("***")
        print("END OF PAGE")
    return wrap

@decor
def invoice(num):
    print("INVOICE #" + num)


invoice("5")
print("===================")

def high(x):
    x = x.lower()
    s = string.ascii_lowercase
    d = {}
    for i in range(len(s)):
        d[s[i]] = i+1
    x = x.split()

    d1 = {}
    for k in x:
        score = 0
        for j in range(len(k)):
            score += d[k[j]]

        d1[k] = score


    return max(d1, key = d1.get)


print(high('man i need a taxi up to ubud'))
print("===================")


def fib(x):
  if x == 0 or x == 1:
    return 1
  else:
    return fib(x-1) + fib(x-2)
print(fib(4))
print("===================")


def convert(num):
    if num==1:
        return 1
    else:
        return (num % 2 + 10 * convert(num // 2))
print(convert(int(input())))


class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + self.level + ")")

name = input()
level = input()
player = Player(name, level)
player.intro()