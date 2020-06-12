class User:
    def work(self):
        print("user do nothing")

class Student(User):
    def work(self):
        print("Student do learning")

class Teacher(User):
    def work(self):
        print("Teacher do Teaching")

class Coder(User):
    def work(self):
        print("Coder do Coding")

student = Student()
print(student.work())

teacher = Teacher()
print(teacher.work())

coder = Coder()
print(coder.work())

user =User()
print(user.work())

student1 =User()
print(student1.work())