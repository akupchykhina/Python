class Table:
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape

    my_property = "test property"

    def get_my_property(self):
        print(self.my_property)


my_table = Table("red", "square")

my_table.get_my_property()
print(my_table.color)
print(my_table.shape)


def search(text, word):
    if word in text:
        return "Word found"
    else:
        return "Word not found"


text = input()
word = input()

print(search(text, word))
