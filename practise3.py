number = [1, 2, 3, 4, 4, 5]

print(2 in number)

number = 7
user_input = input("enter y to enter the game").lower()

if user_input == "y":
    input_number = input("enter your number")
    if input_number == number:
        print("you guess correctly")
    else:
        print("you guess wrong")

else:
    print("thank you for the time")
