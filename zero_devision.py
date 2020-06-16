while True:
    try:
        number = int(input("Enter Your Number ?"))

        try:
            devision = number / 0

        except ZeroDivisionError:
            devision = number / 2

        print(f'the answer is {devision}')
        print('Thank You!')
        break

    except:
        print("Enter valid Number")




