import random

print('###################################')

print('\nThis is a guessing game!!!!')

print('\n###################################')

print('\nGuess a number between 1-10')

print('\nYou have three attempts!!!')

count=random.randint(1,10)
for i in range(count):

    max_attempt = 3
    attempt = 0
    condition = True
    while condition == True:
        if attempt < max_attempt:
            guess = int(input('\nguess the number : '))
            attempt+=1

            if guess == count:
                print('##########CONGRATS##########')
                print('\nyeh you have found the number!!!!!')
                print('\n############################')
                break

            elif guess < count:
                print('\n=> the guess is so low')

            elif guess > count:
                print('\n=> the guess is so high')

        else :
            print('\n=> you are out of attempts')
            break

    choice = input('\nDo you wanna play again??[y/n] : ')
    if choice == 'y':
        condition == True
        count=random.randint(1,10)
        
    elif choice == 'n':
        print('\nYou leaving???')
        print('\nkk bye!!!')
        break