# C200 / Spring 2025
# Lab 03
# Divya Rasania
# drasania

# def square(num):
#     '''
#     number -> number
#     '''
#     return num * num

# print("The square of 7 is", str(square(7)))


def square2(num):               # defines the local variable num
    '''
    number -> number
    '''
    result = num * num          # defines the local variable result
    return result

result = 100

def square4(num):
    '''
    number -> number
    '''
    result = num * num
    # print("We're inside the function square4.")
    # print("Here, the variable result has the value " + str(result))
    return result

# print("Currently, the variable result has the value " + str(result))
# print("We're about to call the function square4.")
# print("square4(1.5) is " + str(square4(1.5)))
# print("We've just finished calling square4.")
# print("Now, result has the value " + str(result))

def double_dash(text):
    '''
    str -> str
    '''
    return text + "-" + text

# the following function takes a width, a height, and a depth and calculates
# the volume of a box with those dimensions.
# number, number, number -> number
def box_volume(width, height, depth):
    '''
    number, number, number -> number
    '''
    return width * height * depth

def square(n):
    """
    returns the square of n
    number -> number
    """
    return n * n
