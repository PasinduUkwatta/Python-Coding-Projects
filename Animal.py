class Animal :
    type ='dog'
    def __init__(self,name,age,colour):
        #in the variable naming we should use _ to tell about the privae variable
        self._name =name
        self._age =age
        self.colour =colour

    def eat(self):
        print(f'{self._name} is a {self.type}, it\'s  {self.colour} colour ')


animal =Animal('sherry',2,'white')
animal.eat()

