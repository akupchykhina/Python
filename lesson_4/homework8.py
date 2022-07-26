class Worker:
    def __init__(self, name, last_name, position, level, salary):
        self.name = name
        self.last_name = last_name
        self.position = position
        self.salary = salary
        self.level = level


    def print_employee(self):
        print(f"{self.name} {self.last_name} works on position {self.position}, level {self.level} with salary {self.salary}")


class Developer(Worker):
    def __init__(self, name, last_name, level, language):
        super(Developer, self).__init__(name, last_name, "developer", level, 80000)
        self.language = language


# class Tester(Worker):
#     def __init__(self, name, last_name, salary, level, language):
#         super(Tester, self).__init__(name, last_name, "tester", salary, level)
#         self.language = language


workerD = Developer("Bob", "Pit", 3, "Python")
# workerT = Tester("Irina", "Babko", 60000, 3, "Java")

workerD.print_employee()


# class BI(Worker):
#     def __init__(self, name):
#         super(BI, self).__init__(name)
#         self.level = 1
#
#     def salary(self):
#         print(110000)
#
#
# class Manager(Worker):
#     def __init__(self, name):
#         super(Manager, self).__init__(name)
#         self.level = 3
#
#     def salary(self):
#         print(250000)

