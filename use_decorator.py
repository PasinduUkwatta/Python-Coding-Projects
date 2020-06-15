def print_stars(func):
    def wrap_func():
        for i in range(10):
            print(i)
            func()
        print('hello world')
    return wrap_func

@print_stars
def print_hi():
    print("hi , welcome to the python programming")



print_hi()