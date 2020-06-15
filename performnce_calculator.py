# decorater

# this will give us the excution time of the code
from time import time


def performance(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'tooks {t2 - t1} secs')
        return result

    return wrap_func


@performance
def long_time():
    for i in range(100000000):
        i = i * 2


long_time()
