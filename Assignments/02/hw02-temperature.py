# C200 / Spring 2025
# Homework Assignment 02
# Divya Rasania
# drasania

def convert_temp():
    '''
    number -> number

    purpose: convert celsius to fahrenheit and fahrenheit to celsius for a given number
    '''
    temp = float(input('Please enter a temperature to convert: '))
    fahrenheit = (temp * (9/5)) + 32
    celsius = (temp - 32) / (9/5)
    print('The converted tempurature is:')
    print(f'{temp} Fahrenheit -> {celsius} Celsius')
    print(f'{temp} Celsius -> {fahrenheit} Fahrenheit')
