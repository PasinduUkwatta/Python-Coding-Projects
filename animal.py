class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):
    def __init__(self, name, age, work):
        super().__init__(name, age)
        self.work = work

    def print_details(self):
        print(f'{self.name} is {self.age} years old & it is {self.work}')


class Cat(Animal):
    def __init__(self, name, age, work):
        # this will initilized the inherited properties from the animal class
        super().__init__(name, age)
        self.work = work

    def print_details(self):
        print(f'{self.name} is {self.age} years old & it is {self.work}')


dog = Dog('Sheery', 2, 'Barking')
cat = Cat('Kitty', 4, 'Sleeping')

dog.print_details()
cat.print_details()
