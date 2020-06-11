class Student:
    is_student = True
    def __init__(self,name,age,marks):
        if(Student.is_student):
            self.name =name
            self.age =age
            self.marks =marks

    def write(self):
        print(f'my name is {self.name}')
        print(f'my age is {self.age}')
        print(f'my marks is {self.marks}')
        return ''

    @classmethod
    def adding_things(cls,num1,num2):
        return ('Tom',num1+num2,num2-num1)

    @staticmethod
    def adding_things2(num1,num2):
        return (num1+num2)



student =Student('Pasindu',24,10)

print(student.write())
print(student.adding_things(3,4))
print((student.adding_things2(6,8)))
student2 =Student.adding_things(9,20)
print(student2)