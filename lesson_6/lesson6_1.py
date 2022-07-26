"""Operator Overloading

We are improving our drawing application.
Our application needs to support adding and comparing two Shape objects.
Add the corresponding methods to enable addition + and comparison using
the greater than > operator for the Shape class.

The addition should return a new object with the sum of the widths and
heights of the operands, while the comparison should return the result
of comparing the areas of the objects.

The given code creates two Shape objects from user input, outputs the
area() of their addition and compares them."""

#
# class Shape:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def __add__(self, other):
#         return Shape(self.width + other.width, self.height + other.height)
#
#     def area(self):
#         return self.width * self.height
#
#
# w1 = int(input())
# h1 = int(input())
# w2 = int(input())
# h2 = int(input())
#
# s1 = Shape(w1, h1)
# s2 = Shape(w2, h2)
# result = s1 + s2
#
# print(result.area())
# print(s1.area() > s2.area())

# class Player:
#     def __init__(self, name, lives):
#         self.name = name
#         self._lives = lives
#
#     def hit(self):
#         self._lives -= 1
#
#     @property
#     def isAlive(self):
#         return self._lives
#
#
# p = Player("Cyberpunk77", int(input()))
# i = 1
# while True:
#     p.hit()
#     print("Hit # " + str(i))
#     i += 1
#     if not p.isAlive:
#         print("Game Over")
#         break


#
# class Pizza:
#     def __init__(self, toppings):
#         self.toppings = toppings
#         self._pineapple_allowed = False
#
#     @property
#     def pineapple_allowed(self):
#         return self._pineapple_allowed
#
#     @pineapple_allowed.setter
#     def pineapple_allowed(self, value):
#         if value:
#             password = input("Enter the password: ")
#             if password == "Sw0rdf1sh!":
#                 self._pineapple_allowed = value
#             else:
#                 raise ValueError("Alert! Intruder!")
#
# pizza = Pizza(["cheese", "tomato"])
# print(pizza.pineapple_allowed)
# pizza.pineapple_allowed = True
# print(pizza.pineapple_allowed)


class Enemy:
  name = ""
  lives = 0
  def __init__(self, name, lives):
    self.name = name
    self.lives = lives

  def hit(self):
    self.lives -= 1
    if self.lives <= 0:
       print(self.name + ' killed')
    else:
        print(self.name + ' has '+ str(self.lives) + ' lives')


class Monster(Enemy):
  def __init__(self):
    super().__init__('Monster', 3)


class Alien(Enemy):
  def __init__(self):
    super().__init__('Alien', 5)


m = Monster()
a = Alien()

while True:
    x = input()
    if x == 'exit':
        break
    elif x == "laser":
        a.hit()
    elif x == "gun":
        m.hit()
