class Alive:

    def __init__(self, breath, eat, reproduce):
        self.breath = breath
        self.eat = eat
        self.reproduce = reproduce


class Mammal(Alive):
    def __init__(self):
        super().__init__("lungs", "milk", "brith")


class Predator(Mammal):
    def __init__(self, eat):
        super().__init__()
        self.eat = eat
        self.feature = "class"


bobcat = Predator("meat")
print(bobcat.breath)

tiger = Mammal()
print(tiger.eat)
print(tiger.breath, tiger.eat, tiger.reproduce)