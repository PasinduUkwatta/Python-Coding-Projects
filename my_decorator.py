#decorator

def my_decorator(func):
    def wrap_func():
        print('**********')
        func()
        print('**********')
    return wrap_func

@my_decorator
def hello():
    print('hello')

@my_decorator
def bye():
    print('bye')

#in this the decorater function will called
#becuse we added the @mydecorater before the funtion
#so then the both codes are execute at the time when run the code
hello()
bye()