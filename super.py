# super() = Function used in a child class to call methods from a parent class ( super class ).
#           allows you to extend the functionality of the inherited methods


class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(
            f'it is {self.color} and {'filled' if self.filled else 'not filled'}')


class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    def describe(self):
        print(
            f" it is a circle with an area of {3.14 * self.radius * self.radius} cm^2")
        super().describe()


class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

    def describe(self):
        print(
            f" it is a square with an area of {self.width * self.width} cm^2")
        super().describe()


class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

    def describe(self):
        print(
            f" it is a triangle with an area of {self.width * self.height / 2} cm^2")
        super().describe()


circle = Circle(color='Red', filled=False, radius=5)
square = Square(color='Blue', filled=False, width=20)
triangle = Triangle(color='Green', filled=True, width=20, height=30)

# circle.describe()
# square.describe()
# triangle.describe()

# print(circle.color, circle.filled, circle.radius)
# print(square.color, square.filled, square.width)
# print(triangle.color, triangle.filled, triangle.width, triangle.height)
