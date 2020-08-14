number = 7
user_responce = input("would you like to play ??").lower()
if user_responce == "y":
    while True:

        num_input = int(input("enter your number"))
        if num_input == number:
            print("you guess correctly")
            break

        else:
            print("you guess wrong")

else:
    print("thnk you for the time")


grades =[55,67,87,43,56]

total =0

for marks in grades:
    total=total+marks

print(total/len(grades))


numbers =[1,2,3,4,5,6,7,8,9]

evens =[]

for num in numbers:
    if(num%2==0):
        evens.append(num)

print(evens)

user_input = input("enter you choice ???").lower()

if user_input =="a":
    print("add")

elif user_input =="q":
    print('quit')

else:
    print("enter again")