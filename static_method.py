#  Static methods = A method that belong to a class rather than any object from that class ( instance)
#                   usually user fro general utility functions


# Instance methods = Best for operations on instance of the class (objects)
# Static Methods = best for utility functions that do not need access to class data


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} =  {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ['Manager', 'Developer', 'Janitor']
        return position in valid_positions


employee1 = Employee('Sheldon', 'Manger')
employee2 = Employee('Leonerd', 'Developer')
employee3 = Employee('Rajesh', 'Janitor')


print(Employee.is_valid_position('Manager'))

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
