class Polygon:
    def __init__(self, sides_count):
        print("Start init Polygon")
        self.sides_count = sides_count
        print("Stop init Polygon")

    def print_number_of_sides(self):
        print(f"It has {self.sides_count} sides")

class Triangle(Polygon):
    def __init__(self):
        print("Start init Triangle")
        super().__init__(3)
        print("Stop init Triangle")

tri = Triangle()