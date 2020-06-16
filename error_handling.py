# Error Handing
# we put the risky code in the try block and the handing code in the except code
while True:
    try:
        age = int(input('Enter Your Age?'))
        print(f'Your Age is  {age}')


    except:
        print("Please enter a number")

    else:
        print('Thank You!')
        break
