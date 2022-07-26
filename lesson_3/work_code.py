import math


# def square_area(A):
#     # your code here
#     #4*A = 2*p*r; r = 4*A / (2*p) = 2*A/p
#     r = 2 * A / math.pi
#     square = r ** 2
#     return square
#
#
# A = int(input())
# print(round(square_area(A), 2))


def sum_mul(n, m):
    sum_mult = 0
    if n != 0 and m != 0 and n < m:
        for i in range(m - 1, n - 1, -1):
            if i % n == 0:
                sum_mult = sum_mult + i
        return sum_mult

    else:
        return "INVALID"


print(sum_mul(2, 9))


def find_multiples(integer, limit):
    lst = []
    for l in range(integer, limit + 1, 1):
        if l % integer == 0:
            lst.append(l)
    return lst


print(find_multiples(5, 25))


def remove_every_other(my_list):
    new_list = my_list[::2]  # удаление каждого второго элемента
    return new_list


print(remove_every_other([1, 2, 2, 3, 4, 5, 6]))


def count_sheep(n):
    for i in range(0, n, 1):
        i += 1
        print(f'{i} sheep...', end="")


count_sheep(5)

print('------------------------')


def count_sheep1(v):
    sheep = ''
    j = 0
    while j in range(v):
        sheep = sheep + f'{j + 1} sheep...'
        j = j + 1
    return sheep


print(count_sheep1(8))

print('------------------------')


def first_non_consecutive(arr):
    for i in range(len(arr) - 1):
        i += 1
        if arr[i] != (arr[i - 1] + 1):
            return arr[i]


print(first_non_consecutive([2, 3, 4, 5, 8, 9, 10, 12]))
# print(first_non_consecutive([2, 3, 4, 5]))

arr1 = [1, 2, 3, 4, 6]
for i in range(len(arr1) - 1):
    i += 1
    if arr1[i] != (arr1[i - 1] + 1):
        print(arr1[i])

print('----------------------------')


def pipe_fix(nums):
    return list(range(nums[0], (nums[-1] + 1)))


print(pipe_fix([2, 8, 9]))
print('----------------------------')


def each_cons(lst, n):
    new_arr2 = []
    i = 0
    while i in range(len(lst) - n + 1):
        x = lst[i:(n + i):1]
        new_arr2.append(x)
        i += 1
        print(x)
    return new_arr2


print(each_cons([1, 5, 5, 6, 9, 8, 15], 3))


def odd_count(n):
    count = n // 2
    return count


print(odd_count(781558368))
print('----------------------------')


def merge_arrays(arr1, arr2):
    new_arr = []
    for a1 in arr1:
        if a1 not in new_arr:
            new_arr.append(a1)
    for a2 in arr2:
        if a2 not in new_arr:
            new_arr.append(a2)
    new_arr.sort()
    return new_arr


print(merge_arrays([1, 2, 3, 4], [1, 2, 3, 5, 6, 9, 7]))
print("----------------------")


def powers_of_two(n):
    lst = []
    for i in range(0, n + 1):
        lst.append(2 ** i)

    return lst


print(powers_of_two(2))


def string_to_array(s):
    return s.split()


print(string_to_array(""))
print("----------------------")


def pillars(num_pill, dist, width):
    distance = dist * (num_pill - 1) + width * (num_pill - 2)
    return distance


print(pillars(2, 20, 25))
print("----------------------")


def string_clean(s):
    s1 = ""
    for n in s:
        if n not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
            s1 = s1 + n
    return s1


print(string_clean("kjnkjnb55gbf,jnib$lmbgkm88mbgkbn3  dgtdgbdfgtv g2542jh9"))
print("----------------------")


def symmetric_point(p, q):
    return [2*q[0]-p[0], 2*q[1]-p[1] ]


p = [1, -35]
q = [-12, 1]
print(symmetric_point(p, q))
print("----------------------")


def remove_char(s):
    return s[1 : -1]


s = "Hello! It is me"
print(remove_char(s))
print("----------------------")


def well(x):
    count = 0
    for i in range(0, len(x)):
        if x[i] == "good":
            count += 1

    if count < 1:
        return 'Fail!'
    if 1 <= count <= 2:
        return 'Publish!'
    else:
        return 'I smell a series!'


x = ["good", "good", "good"]
print(well(x))


def well1(x1):
    c = x1.count('good')
    return 'I smell a series!' if c > 2 else 'Publish!' if c else 'Fail!'


x1 = ["bad", "bad", "good"]
print(well1(x1))
print("----------------------")


str1 = "welcome"
print(str1[::-1])


def fake_bin(x):

    for d in x:
        if d in ("1", "2", "3", "4"):
            x = x.replace(d, "0")
    for d in x:
        if d in ("5", "6", "7", "8", "9"):
            x = x.replace(d, "1")
    return x

print(fake_bin("45385593107843568"))
print("------------------------")


def multi_table(number):
    res = ""
    for i in range(1, 11, 1):
        res += f'{i} * {number} = {i * number}\n'
    return res.strip()


print(multi_table(5))
print("--------------------------------")


def no_space(xx):
    for l in xx:
        if l == " ":
            xx = xx.replace(" ", "")
    return xx

print(no_space("tonya hello"))

print("--------------------------------")


def reverse_func(lst):
    return lst[::-1]


print(reverse_func([1, 2, 3, 4, 5]))

print("--------------------------------")


def highest(lst):
    return [max(lst), max(lst)-1]


print(highest([1, 9, 10]))
print("--------------------------------")

def spin_words(sentence):
    sentence = sentence.split(" ")

    for i in range(len(sentence)):
        if len(sentence[i]) > 4:
            sentence[i] = sentence[i][::-1]


    return " ".join(sentence)

print(spin_words("Hello POl my name is toska"))
print('------------------------')

def high_and_low(numbers):
    n = numbers.split(" ")
    new = ""
    for i in range(len(n)):
        n[i] = int(n[i])

    return f"{max(n)} {min(n)}"

print(high_and_low("5 9 2 1 7"))

text = "input hih nhkj dfdsd"
dict = {}
for i in range(len(text)):
    dict[text[i]] = text.count(text[i])
print(dict)

def disemvowel(string_):
    string = ""
    for s in string_:
        if s not in ("aeiouAEUIO"):
            string = string + s
    return string


print(disemvowel("hello it is fun lol"))
print("------------------")

def get_middle(s):
    l = len(s) % 2
    if l == 1:
        return s[(len(s)//2)]
    else:
        return

print(get_middle("q"))
print("------------------")



