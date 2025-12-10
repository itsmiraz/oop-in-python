# @property = decorator used to define a method as a property (it can be acces like an attribute) benefit: add additonal logic when read write or delete
#           attributes gives you getter , settter and deleter method


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f} cm"

    @property
    def height(self):
        return f"{self._height:.1f} cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print('Width must be greated then zero')

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._width = new_height
        else:
            print('Height must be greated then zero')

    @width.deleter
    def width(self):
        del self._width
        print('Widtht deleted succesffully')

    @height.deleter
    def height(self):
        del self._height
        print('Height deleted succesffully')


rectangle = Rectangle(30, 40)


rectangle.width = 0


del rectangle.width
del rectangle.height
