# Class variable


class Student:

    class_year = 2024
    num_student = 0

    def __init__(self, name, roll, age, ):
        self.name = name
        self.age = age
        self.roll = roll

        Student.num_student += 1


student1 = Student('Miraj', 2, 23)
student2 = Student('Hasan', 1, 22)
student3 = Student('Mehedi', 1, 22)


print(student2.name)
print(student2.age)
print(student2.roll)
print(Student.class_year)


print(
    f"My graduating class of {Student.class_year} has {Student.num_student} students")

print('Num of student:', Student.num_student)
