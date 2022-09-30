########################################################################
##
## CS 101 Lab
## Program #
## Name: Jaxen Woodberry
## Email: jnwmff@umsystem.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed
import random

def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    play = input('Do you want to play again? ==>')
    my_list = ["Y", "YES","N", "NO"]

    if play not in my_list: #when input not in the list stop game
         print("You must enter Y/YES/N/NO to continue. Please try again")
         return play_again
    if (play == "Y") or (play == "Yes"):
        return True
    return False
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    chips = int(input('How many chips do you want to wager? ==>'))

    if (chips == 0):
        print('The wager amount must be greater than 0. Please enter again.')
        return get_wager(bank)
    elif chips > 100:
        print('Too high a value, you can only choose 1 - 100 chips')
        return get_wager(bank)
    elif chips < 1:
        print('Too low a value, you can only choose 1 - 100 chips')
        return get_wager(bank)
    return chips           

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    reel1 = random.randint(1,10)#pick random numbers for slot
    reel2 = random.randint(1,10)
    reel3 = random.randint(1,10)

    return reel1, reel2, reel3

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if (reela == reelb == reelc):
        return 3
    elif (reela == reelb) or (reelb == reelc) or (reela == reelb):
        return 2
    
    return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    start = int(input('How many chips do you want to start with? ==>'))
    if start <= 0 :
        print('The wager amount cannot be less than how much you have.')
        return get_bank()
    elif start > 101:
        print('The wager amount cannot be greater than how much you have.')
        return get_bank()
    
    return 0

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''

    if matches == 3:
        return wager * 10
    if matches == 2:
        return wager *3
   
    return wager * -1
    


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()
        spin = 0
        most = bank
        while True:
            spin = 1 + spin

            if bank < 0:
                break
            elif bank > 0:
                continue
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            
        print("You lost all", 0, "in", spin, "spins")
        print("The most chips you had was", 0)
        playing = play_again()
