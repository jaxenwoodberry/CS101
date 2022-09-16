#welcome
print('Welcome to the Flarsheim Guesser!\n')
user_input = int(input('Please think of a number between and including 1 and 100.\n'))

play_again = 'Y'
to_quit = 'N'
#create loop to run through entire game
while play_again == 'Y':
    print('Please think of a nmumber between and including 1 and 100.')

    three_rem = 0
    five_rem = 0
    seven_rem = 0
#remainder 3 with if/elif statements
    three_rem = int(input('What is the remainder when your number is divided by 3?'))
    while (three_rem < 0 or three_rem > 3):
        if three_rem < 0:
            print('The value entered must be 0 or greater\n')
        elif three_rem > 3:
            print('The value entered must be less than 3\n')
        three_rem = int(input('What is the remainder when your number is divided by 3?'))
    print()
#remainder 5 with if/elif statements
    five_rem = int(input('What is the remainder when your number is divided by 5?'))
    while (five_rem < 0 or five_rem > 5):
        if five_rem < 0:
            print('The value entered must be 0 or greater\n')
        elif five_rem > 5:
            print('The value entered must be less than 5\n')
        five_rem = int(input('What is the remainder when your number is divided by 5?'))
    print()
#remainder 7 with if/elif statements
    seven_rem = int(input('What is the remainder when your number is divided by 7?'))
    while (seven_rem < 0 or seven_rem > 7):
        if seven_rem < 0:
            print('The value entered must be 0 or greater\n')
        elif seven_rem > 7:
            print('The value entered must be less than 7\n')          
        seven_rem = int(input('What is the remainder when your number is divided by 7?'))
    print()

#finding out the remainders
    for i in range(1,101):
       if i%3 == three_rem and i%5 == five_rem and i%7 == seven_rem:
            print(f'Your number was {i}')
            print('How amazing is that?')
            print()
#stop loop from returning to beginning
#play again?
    play_again = input('Do you want to play again? Y to continue, N to quit ==>')
    while (play_again != 'Y' and play_again != 'y' and play_again != 'N' and play_again !='n'):
       play_again = input('Do you want to play again? Y to continue, N to quit ==>')

        


