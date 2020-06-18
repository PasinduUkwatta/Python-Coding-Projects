
#To create a generator we just simply need to add yield keyword 

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
    print('1')
    for i in range(100000000):
        i = i * 2

@performance
def long_time2():
    print('5')
    for i in list(range(100000000)):
        i = i * 2

long_time()
long_time2()

# output
# 1
# tooks 6.012304306030273 secs
# 5
# tooks 31.706650733947754 secs
