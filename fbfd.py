"""
Create a class call student, the student would have an attribute called name.
Each time, a student is initialised, it is allocated with a running student number (student_id)
that starts from 1,
second student number 2 etc.
Add in appropriate string representation for student.
"""

class Student:
    next_id = 1 #class attribute

    def __init__(self, name):
        self.name = name #instance/object attribute
        self.student_id = Student.next_id
        Student.next_id += 1

    def __str__(self):
        return "{}, id={}".format(self.name, self.student_id)

john = Student("John")
print(john) # John id= 1

jane = Student("Jane")
print(jane) # John id= 2

ann = Student("Ann")
print(ann) # John id= 2 