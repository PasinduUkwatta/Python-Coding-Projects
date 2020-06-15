def hello():
    print("hello world")


greet = hello()

del hello

print(greet)


def print_greet(func):
    func()


def greet_func():
    print('welcome to the greet ')


call = print_greet(greet_func)

print(call)
