class Person:
    name = ""
    sex = ""
    dob = ""

    def age(self):
        # pass #своего рода как заглушка, позваляет оставить метод пустым
        return 20

    def get_age(self):
        print(self.age())


person_1 = Person()
person_1.name = "Bob"
person_1.dob = "01/01/2000"

print(person_1.name, person_1.dob)
person_1.get_age()