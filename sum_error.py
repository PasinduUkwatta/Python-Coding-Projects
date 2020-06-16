#from this method we can get the error with the decription
def sum(num1, num2):
    try:
        sum = num1 + num2
        return sum
    except TypeError as error :
        print(f'enter vailid entry : {error}')


print( f'sum is {sum(1, 2)}')
