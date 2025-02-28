# C200 / Spring 2025
# Lab 04
# Divya Rasania
# drasania

def speedometer(pos1, pos2, time):
    """
    Problem Description
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Calculate the speed of the animal.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Input:
        pos1 - the initial position of the animal
        pos2 - the final position of the animal
        time - the recorded time the animal spent between them
    Returns: The speed of the animal.
    """
    return abs((pos1 - pos2) / time)

def animal_average_speed(animal_type):
    """
    Problem Description
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Different types of animals can run at different speeds.
    Using if statements, return the (average) speed of the animal
    based on the type that is given.

    Animal     |  Animal Type |  Average speed (mph)
    ________________________________________________
    Sailfish   |  0           |   68
    Goose      |  1           |   88
    Wildebeest |  2           |   50
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Input: The type of animal
    Returns: Average speed of corresponding animal
    """
    animal = ""
    animal_speed = 0
    
    if animal_type == 0:
        animal = "Sailfish"
        animal_speed = 68
    elif animal_type == 1:
        animal = "Goose"
        animal_speed = 88
    elif animal_type == 2:
        animal = "Wildebeest"
        animal_speed = 50
    else:
        return "Enter a valid animal type"
    
    return animal_speed

def animal_speed_compare(animal1_pos1, animal1_pos2, animal1_time, animal2_type):
    """
    Problem Description
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Make sure to use the first two functions in this file to help you!
    Given the input data for the speed of some animal (animal1), and the type of a *different* animal (animal2),
    return a string based on whether the first animal's speed is greater than the average speed of the other animal.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Input:
        animal1_pos1 - the initial position of the animal
        animal1_pos2 - the final position of the animal
        animal1_time - the time it took for the animal to travel between pos1 and pos2
        animal2_type - the type of animal to compare against
    Returns: "The animal is faster" or "The animal is slower"
    """
    first_animal_speed = speedometer(animal1_pos1, animal1_pos2, animal1_time)
    second_animal_speed = animal_average_speed(animal2_type)

    if first_animal_speed > second_animal_speed:
        return "The first animal is faster"
    elif first_animal_speed == second_animal_speed:
        return "Both animals are at same speed"
    elif first_animal_speed < second_animal_speed:
        return "The first animal is slower"
    else:
        return "Enter valid inputs"

def myTestString(func, params):
    """
    Do not modify
    """
    return func.__name__ + "" + str(params) + " produces " + str(func(*params))

#Examples to see the difference between "print" and "return"
def function_that_prints():
    print("I printed")

def function_that_returns():
    return "I returned"

#   For more information about the line below, refer to the link: https://docs.python.org/3/library/__main__.html
#   You can read more about it but it is to help when handling multiple files
#   Will be dicussed at a later point
if __name__ == "__main__":
    print("Final Test Code\n")
    print("Testing speedometer()")
    for x in [(0.0,400,5.0), (-1,5,0.5), (0,0,1.0), (6,-100,3)]:
        print(myTestString(speedometer, x))
    print("Testing animal_average_speed()")
    for x in [(0,), (1,),(2,), (3,)]:
        print(myTestString(animal_average_speed, x))
    print("Testing animal_speed_compare()")
    for x in [(0.0,400,5.0,1), (0.0,400,5.0,0), (25,150,1.0,2)]:
        print(myTestString(animal_speed_compare, x))
