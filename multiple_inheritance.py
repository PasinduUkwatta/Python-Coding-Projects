class User:
    def sign_in(self):
        print("user sign in")

class NewPlayer(User):
    def __init__(self,name,age,power):
        self.name =name
        self.age =age
        self.power =power

class MiddlePlayer(User):
    def __init__(self,name,age,marks):
        self.name =name
        self.age =age
        self.marks =marks

#in the multiple inheritance we need to intilialize each inherited things seperatly
class ProPlayer(NewPlayer,MiddlePlayer):
    def __init__(self,name,age,power,marks,rank):
        NewPlayer.__init__(self,name,age,power)
        MiddlePlayer.__init__(self,name,age,marks)

        self.rank =rank

    def print_details(self):
        print(f'{self.name} is {self.age} years old , he has {self.power} power and {self.marks} marks , his rank is {self.rank} ')


proPlayer = ProPlayer('Pasindu',24,'water',1000,1)
proPlayer.print_details()