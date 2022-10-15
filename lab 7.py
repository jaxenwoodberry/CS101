##Jaxen Woodberry
##CS 101 Lab
##Program 7

def get_minimum_mpg(): #function defined to find min miles per gal
    while True:
        try:
            min_mpg = float(input('Enter the minimum mpg ==>'))
            if min_mpg <= 0: #fuel economy cannot be less than or zero
                print('Fuel economy given must be greater than 0')
                continue
                #maybe add continue because instructions say 'it should continually ask for correct value???
            elif min_mpg >= 100: #fuel economy cannot be 100 or more
                print('Fuel economy must be less than 100')
                continue
            else:
                print()
                return min_mpg
        except ValueError: #prevents input that is not numerical
            print('You must enter a number for the fuel economy')

def get_file_input():
    while True:
        try:
            user_input = input('Enter the name of the input vehicle file ==>')
            file_input = open(user_input, 'r')
            print()
            return file_input
        except FileNotFoundError:
            print(f'Could not open file {user_input}')

def get_file_output():
    while True:
        try:
            user_output = input('Enter the name of the file to output to ==>')
            file_output = open(user_output, 'w') #w instead of r to write file instead of read
            print()
            return file_output
        except IOError:
            print(f'There is an IO Error {user_output}')
            print(f'Could not convert {elements[3]} for vehicle {element[0]} {element[1]}')

if __name__ == "__main__":
    min_mpg = get_minimum_mpg()
    file_input = get_file_input()
    file_output = get_file_output()
    lines = file_input.readlines()
    for line in lines:
        elements = []
        elements = line.split('\t')
        try:
            if float(elements) >= min_mpg:
                file_out.write(f'{elements[0]} {elements[1]}     {elements[2]}                  {elements[3]:.3f}\n')
            else:
                continue
        except ValueError:
            print(f'Could not convert {elements[3]} for vehicle {element[0]} {element[1]} {element[2]}\n')