class User():
    def sign_in(self):
        print("user login to the system")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"{self.name} attacking with the power of {self.power}")
        return ''


class Archer(User):
    def __init__(self, name, bow):
        self.name = name
        self.bow = bow

    def attack(self):
        print(f"{self.name} attacking with the power of {self.bow}")
        return ''


class Hunter(User):
    def __init__(self, name, knife):
        self.name = name
        self.knife = knife

    def attack(self):
        print(f"{self.name} attacking with the power of {self.knife}")
        return ''


wizard = Wizard('john', 'water')
print(wizard.attack())

archer = Archer('robin', 'wood')
print(archer.attack())

hunter = Hunter('gwen', 'steel')
print(hunter.attack())

#this will check about the instances of the class
#wizard is a child class of the user
#so it is a instance
print(isinstance(wizard,User))