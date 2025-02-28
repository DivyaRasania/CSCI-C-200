# C200 / Spring 2025
# Homework Assignment 02
# Divya Rasania
# drasania

def mersenne():
    '''
    purpose: takes a number and outputs 2^(n) - 1
    '''
    # variables
    mersennedList = []

    # taking input, splitting at ' ' and making a tuple
    numList = tuple(input("Enter a list of numbers(eg. 1 2 3): ").split(' '))

    # iterating inside numList tuple
    for i in numList:
        # making it mersenne numbers and adding them to mersennedList
        # casting 'i' to int so it can be used for this calculations
        mersennedList.append(2**(int(i))-1)
        # casting 'i' back to string so it can be used by for loop
        str(i)

