import math

#problem 1
#input real number
#return real number
def g(x):
    '''
    Given a real number x, return the value of the function g(x) defined by:

    Args:
        number

    Returns: 
        number
    '''

    if x != 0:
        result = x + 2
    elif x == 0:
        result = 1
    else:
        result = None
    
    return result


#problem 2
#input year 1977-1997
#return percent income or "error: year" if year 
#is outside range
def cost(t):
    '''
    Given a year t, return the percent of income spent on housing in that year.

    Args:
        year: number
    
    Returns:
        percent: number
    '''
    percent = 0.0

    if 1977 <= t <= 1984:
        percent = (2 / 7) * (t - 1977) + 12
    elif 1984 < t <= 1987:
        percent = (t - 1977) + 7
    elif 1987 < t <= 1997:
        percent = (3 / 5) * (t - 1977) + 11
    else:
        return "error: year"

    return percent

#problem 3
#round to 2 decimal places
#input t years = 0, 1, then 2
#output dollars
def oem(t):
    '''
    Find the difference between OEM0 and OEM1.

    Args:
        t: number

    Returns:
        dollars: string
    '''
    return round(oem_0(t) - oem_1(t), 2)

def oem_1(t):
    '''
    Find the cost of non OEM parts for the same years.

    Args:
        t: number

    Returns:
        number
    '''
    return (26 * (((1 / 4) * (t ** 2) - 1) ** 2) + 52)

def oem_0(t):
    '''
    Find the cost of OEM parts for year t = 0, year t = 1, and year t = 2.

    Args:
        t: number

    Returns:
        number
    '''
    return (110 / ((1 / 2) * t + 1))

#problem 4
#input tuple (a,b,c) coefficients
#output tuple roots (x_1, x_2) where x_1 >= x_2
def quad(coefficients):
    '''
    Given a tuple of coefficients, return the roots of the quadratic equation.

    Args:
        coefficients: tuple

    Returns:
        roots: tuple
    '''
    a = coefficients[0]
    b = coefficients[1]
    c = coefficients[2]
    x = y = 0

    x = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    y = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)

    return (x, y)

#problem 5
#input [arg1,op,arg2,ans]
#output arg1 op arg2 == ans
def expr_eq(lst):
    '''
    Given a list of arguments, return whether the expression is true or false.

    Args:
        lst: list

    Returns:
        boolean
    '''
    arg1 = lst[0]
    op   = lst[1]
    arg2 = lst[2]
    ans  = lst[3]

    return True if eval(f'{arg1} {op} {arg2}') == ans else False

#problem 6
#input string of COVID symptoms "ABC", "ACB",...,"CBA"
#output 'very likely', 'likely', 'somewhat likely' based on severity
def chance_of_covid(symptoms):
    '''
    Given a string of COVID symptoms, return the likelihood of having COVID.

    Args:
        symptoms: string

    Returns:
        likelihood: string
    '''
    first_symptom  = symptoms[0]
    second_symptom = symptoms[1]
    third_symptom  = symptoms[2]
    likelihood     = None

    if first_symptom[0] == 'A':
        likelihood = 'very likely'
    elif first_symptom[0] == 'B':
        likelihood = 'likely'
    else:
        likelihood = 'somewhat likely'
    
    return likelihood

#problem 7
#INPUT two numbers
#RETURN maximum of the two
#You cannot use Python's max function
#You must use if, elif, else (or some combination)
def max2d(x,y):
    '''
    Given two numbers, return the maximum of the two.

    Args:
        x: number
        y: number

    Returns:
        number
    '''
    return x if x > y else y

#INPUT 3 numbers
#RETURN maximum of the three
#You must use your max2D function
def max3d(x,y,z):
    '''
    Given three numbers, return the maximum of the three using max2d function.

    Args:
        x: number
        y: number
        z: number

    Returns:
        number
    '''
    return max2d(x, max2d(y, z))

#problem 8

line = {'slope':None, 'intercept':None}

# You don't have to change this function, we have already completed the clear_line() function for you.
# but you are welcome to see what it does.
#input line dictionary
#assigns None to both keys
#return True
def clear_line(line):
    '''
    Given a line dictionary, set the slope and intercept to None.
    
    Dictionary -> Bool
    '''
    line['slope'] = line['intercept'] = None
    return True

#input two tuples p0 = (x0,y0), p1 =(x1,y1), dictionary line
#output returns dictionary with keys assigned to slope, intercept
#unless the slope is undefined--in this case, return the dictionary
#unchanged
def build_line(p0,p1,line):
    '''
    Given two points, return the slope and intercept of the line.

    Args:
        p0: tuple
        p1: tuple
        line: dictionary

    Returns:
        line: dictionary
    '''
    x0 = p0[0] # x1
    y0 = p0[1] # y1
    x1 = p1[0] # x2
    y1 = p1[1] # y2
    slope = 0 # m
    intercept = 0 # b

    if x1 - x0 != 0:
        slope = (y1 - y0) / (x1 - x0)
    else:
        return line
    
    intercept = y0 - (slope * x0)

    line['slope'] = slope
    line['intercept'] = intercept

    return line

#input dictionary
#output return -(1/m) if slope is defined, otherwise return 'Error: no slope'
def inverse_slope(line):
    '''
    Given a line dictionary, return the inverse of the slope.

    Args:
        line: dictionary

    Returns:
        number
    '''
    slope = line['slope']

    if slope:
        return -(1 / slope)
    else:
        return 'Error: no slope'

#input three tuples 
#output True if colinear, False otherwise
def colinear(p0,p1,p2):
    '''
    Given three points, return whether they are colinear.

    Args:
        p0: tuple
        p1: tuple
        p2: tuple

    Returns:
        boolean
    '''
    line = {'slope':None, 'intercept':None}
    
    build_line(p0, p1, line)
    
    if line['slope'] is None:
        return p2[0] == p0[0]
    
    expected_y = line['slope'] * p2[0] + line['intercept']

    return True if p2[1] == expected_y else False
    # return math.isclose(p2[1], expected_y, abs_tol=0.001)

#problem 9
#INPUT three values: all have values or two have values and the remain has None
#OUTPUT for two values, return the computed None variable
#for three values return True or False using isclose(x,y,abs_tol = 0.001)
#remember to convert degrees to radians
def solve(theta,opposite,adjacent):
    '''
    Given three values, return the missing value or whether the values are close.

    Args:
        theta: number
        opposite: number
        adjacent: number

    Returns:
        theta_angle: number
        opposite_length: number
        adjacent_length: number
         OR
        is_equation: boolean
    '''

    if theta == None:
        theta_angle = math.degrees(math.atan(opposite / adjacent))
        return theta_angle
    elif opposite == None:
        opposite_length = math.tan(math.radians(theta)) * adjacent
        return opposite_length
    elif adjacent == None:
        adjacent_length = opposite / math.tan(math.radians(theta))
        return adjacent_length
    else:
        x = math.tan(math.radians(theta))
        y = opposite / adjacent
        is_equation = math.isclose(x, y, abs_tol=0.001)
        return is_equation

#problem 10
#INPUT List of numbers
#RETURN Various means
def mean(lst):
    '''
    Given a list of numbers, return the mean.

    Args:
        lst: list

    Returns:
        mean_num: number
    '''
    added_num = 0
    total_num = 0
    mean_num = 0

    for i in lst:
        added_num += i
        total_num += 1

    mean_num = added_num / total_num

    return round(mean_num, 2)

def var(lst):
    '''
    Given a list of numbers, return the variance.

    Args:
        lst: list

    Returns:
        variance: number
    '''
    variance = 0
    u = mean(lst)
    total_num = len(lst)

    some_lst = []
    for i in lst:
        some_lst.append((i - u) ** 2)

    some_lst_plus = 0
    for j in some_lst:
        some_lst_plus += j

    variance = (1 / total_num) * some_lst_plus

    return round(variance, 2)

def std(lst):
    '''
    Given a list of numbers, return the standard deviation.

    Args:
        lst: list

    Returns:
        standard_deviation: number
    '''
    return round(math.sqrt(var(lst)), 2)

def mean_centered(lst):
    '''
    Given a list of numbers, return mean minus each value in the list.

    Args:
        lst: list
    
    Returns:
        mean_centered_lst: list
    '''
    mean_num = mean(lst)
    mean_centered_num = 0
    mean_centered_lst = []

    for i in lst:
        mean_centered_num = i - mean_num
        mean_centered_lst.append(mean_centered_num)
    
    return mean_centered_lst

#problem 11
def fibonacci(n):
    '''
    Given a number n, return the nth Fibonacci number.

    Args:
        n: number

    Returns:
        fibonacci_num: number
    '''
    fibonacci_num = 0

    if n > 1:
        a, b = 0, 1
        for _ in range(n - 1):
            fibonacci_num = a + b
            a = b
            b = fibonacci_num
    elif n == 1:
        fibonacci_num = 1
    elif n == 0:
        fibonacci_num = 0
    else:
        return 'Please enter positive integer'
        
    return fibonacci_num

def tribonacci(n):
    '''
    Given a number n, return the nth Tribonacci number.

    Args:
        n: number

    Returns:
        tribonacci_num: number
    '''
    tribonacci_num = 0

    if n > 2:
        a, b, c = 0, 0, 1
        for _ in range(n - 2):
            tribonacci_num = a + b + c
            a = b
            b = c
            c = tribonacci_num
    elif n == 2:
        tribonacci_num = 1
    elif n == 1:
        tribonacci_num = 0
    elif n == 0:
        tribonacci_num = 0
    else:
        return 'Please enter positive integer'
        
    return tribonacci_num

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the unit testing Feel free to add print statements. 
    You should uncomment *after* you've completed the function and comment it back
    before submitting to the Autograder. 
    """

    #problem 1 
    # print(g(0))
    # print(g(1))
    # print(g(1.01))

    #problem 2
    # print(cost(1976))
    # print(cost(1977))
    # print(cost(1985))
    # print(cost(1988))
    # print(cost(2000))

    #problem 3
    # print(oem(0))
    # print(oem(1))
    # print(oem(2))

    #problem 4
    # print(quad((1,0,-1)))
    # print(quad((6,-1,-35)))
    # print(quad((1,-7,-7)))

    #problem 5
    # print(expr_eq([14, "/",2, 7]))
    # print(expr_eq([20, "*",19, 381]))
    # print(expr_eq([20, "*",19, 380]))
    # print(expr_eq([1.1,'-',1,.1])) #saw in class this doesn't work! (will return False)

    #problem 6
    # print(chance_of_covid('ABC'),chance_of_covid('ACB'))
    # print(chance_of_covid('BAC'),chance_of_covid('BCA'))
    # print(chance_of_covid('CAB'),chance_of_covid('CBA'))

    #problem 7
    # print(max3d(1,2,3))
    # print(max3d(1,3,2))
    # print(max3d(3,2,1))

    #problem 8
    # print(line)
    # build_line((2,3),(8,6),line)
    # print(line)
    # clear_line(line)
    # print(line)
    # build_line((2,3),(2,5),line) #not a line
    # print(line)

    # clear_line(line)
    # build_line((-3,2),(4,-1),line)
    # print(line)
    # print(inverse_slope(line))
    # print(colinear((-2,1),(1,7),(4,13)))

    #problem 9
    # print(solve(5,None,105600))
    # print(solve(None,9238.9,105600))
    # print(solve(5,9238.8,None))
    # print(solve(5,9238.8,105600))
    # print(solve(5,9100,105600))

    #problem 10
    # lst = [1,3,3,2,9,10]

    # print(mean(lst))
    # print(var(lst))
    # print(std(lst))
    # print(mean(mean_centered(lst)))

    #problem 11
    # for i in range(10):
    #     print(fibonacci(i))

    # for i in range(10):
    #     print(tribonacci(i))
