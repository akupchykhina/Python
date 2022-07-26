lst = [('test 1', 'log in'), ('test 2', 'log out')]

print(lst)


def test_tuple(tu):
    print(f'My list:\n {tu[0]} : {tu[1]}')


lst.append(('test 3', 'close browser'))

print(lst)

for l in lst:
    print(l)
    for t in l:
        print(t)

print('---------------------------')

string = 'Hello world! I like python! I like world!'
print(string[::-1]) #вывести строку в обратном порядке

print(string.count('e')) #посчитать количество букв е
print(string.count('like'))