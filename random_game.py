import random
import sys
#using sys.argv[] , we can get input from the user
number = random.randrange(int(sys.argv[1]), int(sys.argv[2]))

print("Enter you Number")
while True:
    user_number = int(input("The number is :"))
    if (0<user_number < 10):
        if (user_number == number):
            print('your genius')
            break
        else:
            print('try again')

    else:
        print("enter number between 1 to 10")
