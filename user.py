class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Customer(User):
    def __init__(self, name, age, items):
        super().__init__(name, age)
        self.items = items

    def print_details(self):
        print(f'{self.name} is {self.age} years old &  ordered {self.items}')


class Seller(User):
    def __init__(self, name, age, sells):
        super().__init__(name, age)
        self.sells = sells

    def print_details(self):
        print(f'{self.name} is {self.age} years old &  sells {self.sells}')


class Delivery_Person(User):
    def __init__(self, name, age, delivery):
        super().__init__(name, age)
        self.delivery = delivery

    def print_details(self):
        print(f'{self.name} is {self.age} years old &  deliver {self.delivery}')


customer = Customer('Pasindu', 24, 'Flour,Suger,Rice')
seller = Seller('Saman', 48, 'Milk,Eggs')
delivery_person = Delivery_Person('John', 32, 'Pizza,Fride Rice')

customer.print_details()
seller.print_details()
delivery_person.print_details()
