def print_design(func):
    def pattern():
        for i in range(3):
            for j in range(0,10,3):
                print('*', end='')
                func()

            print('')
    return pattern

@print_design
def hello():
    print('hello')

hello()

