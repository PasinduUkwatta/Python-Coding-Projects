try:
    with open('sad.txt',mode='r') as my_file_3:
        print(my_file_3.read())

except FileNotFoundError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print('file does nor exist')
    raise err
