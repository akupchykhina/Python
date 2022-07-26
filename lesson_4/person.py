# public, protected, private

class Person:
    def __init__(self, name, dob, gender, height, weight):
        self.name = name
        self.__dob = dob #двойное подчеркивание делаем этот параметр неизменным
        self.gender = gender
        self.position = height
        self.weight = weight

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.__dob

    def set_dob(self, new_dob):   #этот метод позваляет изменить неизменяемый параметр в случае ошибки
        self.__dob = new_dob

person1 = Person("Bob", "09/01/2000", "Male", 172, 72)

print(person1.get_name())
print(person1.get_dob())
person1.set_dob("01/01/2000")
print(person1.get_dob())

