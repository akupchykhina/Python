class McDonalds():
    director = "Bob McKinney"
    def __init__(self, name, salary, position, state):
        self.name = name
        self.salary = salary
        self.position = position
        self.state = state

    def print_employee(self):
        print(f"Director name is: {McDonalds.director}", f"Employee name is: {self.name}",
              f"{self.name} salary is: {self.salary}", f"{self.name} position is: {self.position}, {self.state}",
              "---------------------------", sep="\n")


class Pensilvania(McDonalds):
    def __init__(self, name, salary, position):
        super().__init__(name, salary, position, "PA")


class California(McDonalds):
    def __init__(self, name, salary, position):
        super().__init__(name, salary*1.2, position, "CA")


employeeP = Pensilvania("Ivan Pupkin", 55000, "kitchen")
employeeC = California("Pola Pit", 60000, "host")

employeeP.print_employee()
employeeC.print_employee()