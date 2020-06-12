class Toy:
    def __init__(self, colour, age):
        self.colour = colour
        self.age = age

    # in this we override the dunder method to our need
    def __str__(self):
        return f'{self.colour}'

    def __len__(self):
        return 2


action_figure = Toy('blue', 2)

# this is a dunder method
# they can  idntify by '__' sign beforeand after the name
print(action_figure.__str__())
print(action_figure.__len__())
