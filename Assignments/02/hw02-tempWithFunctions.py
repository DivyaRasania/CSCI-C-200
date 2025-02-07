# C200 / Spring 2025
# Homework Assignment 02
# Divya Rasania
# drasania

def fromCtoF(celsius):
    '''
    number -> number

    purpose: convert celsius to fahrenheit
    '''
    # Converting celsius to fahrenheit using formula F = C * 9/5 + 32
    fahrenheit = (celsius * (9/5)) + 32

    # returning the fahrenheit value back
    return fahrenheit

def fromFtoC(fahrenheit):
    '''
    number -> number

    purpose: convert fahrenheit to celsius
    '''
    # Converting fahrenheit to celsius using formula C = (F - 32) ÷ (9/5)
    celsius = (fahrenheit - 32) / (9/5)

    # returning the celsius value back
    return celsius

# assigning tempuratures
celsius = 20
fahrenheit = 73

# printing the calcuated tempuratures using print and f strings
print(f'{celsius} Celsius converted to Fahrenheit is: {fromCtoF(celsius)}')
print(f'{fahrenheit} Fahrenheit converted to Celsius is: {fromFtoC(fahrenheit)}')
