# Nested class = A class defined with another class
#               class Outer:
#                   class Inner:


# Benefits : Allows you to logically group classes that are closely related encapsulates private details that aren't relevant to the outer class
# keeps names clean reduces the possibility of naming conflicts


class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} : {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name=name, position=position)
        self.employees.append(new_employee)

    def list_employee(self,):
        # return [f"{employee.name}" for employee in self.employees]
        return [employee.get_details() for employee in self.employees]


company1 = Company('Resdium')
company2 = Company('Musemind')

company1.add_employee('Miraj', "Developer")
company1.add_employee('Mehedi', "Designer")
company1.add_employee('Hasn', "HR")

company2.add_employee('Sheldon', "Designer")
company2.add_employee('Leonerd', "Manger")

# print()
for employee in company2.list_employee():
    print(employee)
