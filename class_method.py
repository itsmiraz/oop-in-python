#  Class methods = Allow operations related to the class itself take (cls) as the fist parameter, which represents the class itself
#                   Take (cls ) as the first parameter , which represents the class itself


class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

     # instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"

    # class methods

    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"

    @classmethod
    def get_avg_cgpa(cls):
        if cls.count == 0:
            return 0

        else:
            return f"{cls.total_gpa / cls.count:.2f}"


student1 = Student('Miraj', 4.5)
student3 = Student('Sheldon', 3.5)
student2 = Student('Leonerd', 4.32)


print(Student.get_count())
print(Student.get_avg_cgpa())
