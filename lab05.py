########################################################################
##
## CS 101 Lab
## Program #
## Name: Jaxen Woodberry
## Email: jnwmff@umsystem.edu
##
## PROBLEM : User supposed to input the number of chips to gamble between 1 and 100, then add chips to bank.
##
## ALGORITHM : 
##      1. User asked to input number of chips they want to start with between 1 and 100 (inclusive)
##      2. User asked how many chips they want to wager based on how many they have.
##      3. Results of the spin is output along with the number of reels that match, how many chips were won/lost, and the current amount in the bank.
##      4. Steps 2 and 3 are repeated until bank amount reaches 0
##      5. Chips lost is output as well as total spins and the max amount of chips had
##      6. User is asked if they want to play again
##      7. If input is "yes" then above steps are repeated
##      8. If input is "no" then program ends
## ERROR HANDLING:
##      Wager must be between 1 and amount in the bank
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed
import random

def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    while True:
    
        play = input('Do you want to play again? ==>')
        my_list = ["Y", "YES","N", "NO"]
        play = play.upper()
        if (play == 'Y' or play == 'YES'):
            return True
        elif(play == 'N' or play == 'NO'):
            return False
        print('You must enter Y/YES/N/NO to continue. Please try again')
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    while True:
        chips = int(input('How many chips do you want to wager? ==>'))
        if (chips < 0):
            print('The wager amount must be greater than 0. Please enter again.')
        elif (chips > chips):
            print('The wager amount cannot be greater than how much you have.')
        
        else:
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
    while True:
        start = int(input('How many chips do you want to start with? ==>'))
        if(start > 0) and (start < 101):
            return True
        elif start < 1:
            print('Too low a value, you can only choose 1 - 100 chips')
        else:
            print('Too high a value, you can only choose 1 - 100 chips')
    
    

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
        initialbank = bank
        spin = 0
        newbank = 0
        most = bank
        while bank > 0:
            
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
            spin += 1
        print("You lost all",initial bank, "in", spin, "spins")
        print("The most chips you had was", most )
        playing = play_again()
