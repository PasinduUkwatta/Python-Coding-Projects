class PlayerCharactor:
    #this is a staic method
    #all objects have access for this
    membership = True
    def __init__(self,name):
        self.name=name

#we need to provide return value in the function
    #else we will get None after the function execute
    def run(self):
        print('run')
        return 'done'

player1 =PlayerCharactor('cindy')

print(player1.name)
print(player1.membership)
print(player1.run())
