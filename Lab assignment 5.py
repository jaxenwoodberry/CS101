########################################################################
##
## CS 101 Lab
## Program #5
## Jaxen Woodberry
## jnwmff@umsystem.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Start by outputting the proper format for the library card check
##      2. Ask user to input library card or enter to exit program. The function is called that checks multiple conditions;
##      1)That length of input is 10 characters, 2)That the first five characters are A-Z, 3)That the last 3 characters must
##      be 0-9, 4)That the sixth character must be 1 2 ofr 3, 5)That the seventh character musst be 1 2 3 or 4, 6)That the last
##      check digit matches the calculate value.
##      3. If card input is valid then the program will output the school and grade of the card's owner.
##      4. If card not valid then program outputs error as to why.
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
import string


def character_value(ch : str) -> int:
    '''returns A as 0, B as 1, C as 2, etc.'''
    return string.ascii_uppercase.index("A")

def get_check_digit(num : str) -> int:
    '''returns check digit for name and dept.'''
    checkdig = 0
    for index, value in enumerate(num[0:5]):
        checkdig += (character_value(value) * (index + 1))
    for index, value in enumerate(num[5:9]):
        checkdig += (int(value) * (index + 6))
    return checkdig % 10

def verify_check_digit(num : str) -> tuple:
    '''returns true if check digit is valid and false if not'''
    if len(num) != 10:
        return False, 'The length of the number given must be 10'
    for index, value in enumerate(num[0:5]):
        if not value.isalpha():
            return False, 'The first 5 charcters must be A-Z, the invalid character is at {} is {}'.format(index, value)
    for index, value in enumerate(num[7:]):
        if not value.isdigit():
            return False, 'The last 3 charcters must be 0-9, the invalid character is at {} is {}'.format((index + 7), value)
    if get_school(num) == 'Invalid School':
        return False, 'the sixth character must be 1 2 or 3'
    if get_grade(num) == 'Invalid Grade':
        return False, 'the seventh character must be 1 2 3 or 4'
    elif get_check_digit(num) != int(num[9]):
        return True, ''

def get_school(num : str) -> str:
    '''returns school withindex value'''
    schools = {'1' : 'School of Computing and Engineering SCE','2' : 'School of Law','3' : 'College of Arts and Sciences'}
    if num[5] in schools:
        return schools[num[5]]
    else:
        return 'Invalid School'

def get_grade(num : str) -> str:
    '''returns for academic grade'''
    grade = {'1' : 'Freshman','2' : 'Sophomore','3' : 'Junior','4' : 'Senior'}
    if num[6] in grade:
        return grade[num[6]]
    else:
        return 'Invalid Grade'





if __name__ == "__main__":

    print('{:^60}'.format('Linda Hall'))
    print('{:^60}'.format('Library Card Check'))
    print('='*60)


    while True:
        print()
        card = input('Enter Library Card. Hit Enter to Exit ==>').upper()
        if card == '':
            break
        results, error = verify_check_digit(card)
        if results == True:
            print('Library card is valid')
            print('The card belongs to a student in {}'.format(get_school(card)))
            print('The card belongs to a {}'.format(get_grade(card)))
        else:
            print('Library card is invalid.')
            print(error)

    
    
