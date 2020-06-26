import random


number =random.randint(1,10)


while True:
    try :
        guess = int(input('Guess the the number :'))
        if(1<guess<11):
            if guess==number:
                print('Your guess is Correct')
                break

            else:
                print('Try again')
        else:
            print('Enter number in range of 1-10')

    except ValueError :
        print('Please enter a number')
        continue
