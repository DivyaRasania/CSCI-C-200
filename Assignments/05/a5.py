import math

###########################################################################
# Functions for Problem 1
###########################################################################
#INPUT pair of wind velocity, height 
#OUTPUT constant P value
def P_ws(v0,h0,v1,h1):
    """Calculates the constant P value based on wind velocities (v0,v1) and heights (h0,h1), returns a rounded float."""
    P = (math.log(v0 / v1)) / (math.log(h0 / h1))
    return round(P, 3)

###########################################################################
# Functions for Problem 2
###########################################################################
#INPUT dlst = [day, month, year]
#RETURN string corresponding to the day of the week (i.e. "Mon", "Sun", etc)
week = {1:"Mon", 2:"Tue", 3:"Wed", 4:"Thu", 5:"Fri", 6:"Sat", 7:"Sun"}
def a(dlst):
    """Calculates the adjusted year based on the date list [day, month, year], returns an integer."""
    m = dlst[1]
    y = dlst[2]
    return y - ((14 - m) / 12)

def b(dlst):
    """Calculates an intermediate value for day of week calculation based on date list, returns a floor integer."""
    x = a(dlst) + (a(dlst) / 4) - (a(dlst) / 100) + (a(dlst) / 400)
    return math.floor(x)

def c(dlst):
    """Calculates the adjusted month for day of week algorithm based on date list, returns an integer."""
    m = dlst[1]
    return m + 12 * ((14 - m) / 12) - 2

def day(dlst):
    """Determines the day of week from a date list [day, month, year], returns a string abbreviation (e.g. 'Mon')."""
    d = dlst[0]
    day_calculated = (d + b(dlst) + (31 * (c(dlst) / 12))) % 7
    return week[day_calculated]

###########################################################################
# Functions for Problem 3
###########################################################################
#INPUT portfolio of stock price, shares, market
#OUTPUT current total value
def value(portfolio, market):
    """Calculates the percent change between portfolio purchase value and current market value, returns a rounded float."""
    portfolio_value = 0
    market_value = 0
    
    stocks = portfolio.get('stock', {})
    
    for stock_name, (purchase_price, shares) in stocks.items():
        current_price = market.get(stock_name, 0)
        
        stock_portfolio_value = purchase_price * shares
        stock_market_value = current_price * shares
        
        portfolio_value += stock_portfolio_value
        market_value += stock_market_value
    
    if portfolio_value == 0:
        return 0 
    
    percent_change = ((market_value - portfolio_value) / portfolio_value) * 100
    return float(round(percent_change))

###########################################################################
# Functions for Problem 4
###########################################################################
#INPUT a (possibly empty) list of numbers
#OUTPUT raise exception or smooth
def smooth(lst):
    """Averages adjacent values in a list, returns a new list or error message for empty lists."""
    if len(lst) > 1:
        smoothed_lst = []
        for i in range(len(lst) - 1):
            current_num = lst[i]
            next_num = lst[i + 1]
            smoothed_lst.append(round((current_num + next_num) / 2, 2))
        return smoothed_lst
    elif len(lst) == 1:
        return [lst[0]]
    else:
        return "AveError: list empty"

###########################################################################
# Functions for Problem 5
###########################################################################
def msi(x):
    """Finds the maximum sum subarray in a list, returns [start_index, end_index, max_sum]."""
    max_sum = current_sum = x[0]
    max_start = max_end = current_start = 0
    
    for i in range(1, len(x)):
        if current_sum < 0:
            current_start = i
            current_sum = x[i]
        else:
            current_sum += x[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            max_start = current_start
            max_end = i

    return [max_start, max_end, max_sum]

###########################################################################
# Functions for Problem 6
###########################################################################
#root finding formula for algorithm
def f0(x):
    """
    Custom formula, this will just do an operation of 1/(#root finding formula for algorithm e^x)

    int or float -> float
    """
    return math.exp(-x)

def f1(x):
    """
    Custom formula, this will return a f(x) value based on the equation below

    float or int -> float
    """
    return math.sqrt(4*x + 7)

def f2(x):
    """
    Custom formula for finding where x^4 - 4x - 7 = 0
    
    float or int -> float
    """
    return x**4 - 4*x - 7

def f3(x):
    """
    Custom formula for finding where x^5 - 3(x^2) - 2 = 0
    
    float or int -> float
    """
    return x**5 - 3*(x**2) - 2

# input function that finds x and initial guess
# output approximate positive root
def approx_root(f, initial_guess):
    """
    Find an approximate root of function f using Newton-Raphson method
    starting from the initial_guess
    
    (function, number) -> float
    """
    epsilon = 1e-7  # Convergence threshold
    max_iterations = 100
    x = initial_guess
    
    # Fixed-point iteration method to find where f(x) = 0
    for i in range(max_iterations):
        # For functions like f0 where we need to find x = e^(-x)
        if f == f0:
            x_new = f(x)  # For fixed point problems where we need to find x = f(x)
            if abs(x_new - x) < epsilon:
                return x_new
            x = x_new
        # For functions where we need to find roots (f(x) = 0)
        else:
            # Newton-Raphson method
            h = 0.00001  # Small value for numerical differentiation
            # Approximating f'(x) using (f(x+h) - f(x))/h
            derivative = (f(x + h) - f(x)) / h
            
            # If derivative is too close to zero, adjust x slightly
            if abs(derivative) < epsilon:
                x += 0.1
                continue
                
            x_new = x - f(x) / derivative
            
            if abs(x_new - x) < epsilon:
                return x_new
            x = x_new
    
    return x  # Return the best approximation after max iterations

if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You **do not** have to put anything here
    """

    # #problem 1
    # v0 = 25
    # h0 = 200
    # v1 = 6
    # h1 = 35
    # print(P_ws(v0,h0,v1,h1))

    # #problem 2
    # print(day([14,2,2000]))
    # print(day([14,2,1963]))
    # print(day([14,2,1972]))

    #problem 3
    # portfolios = {'A':{'stock':{'x':(41.45, 45),'y':(22.20, 1000)}}, 'B':{'stock':{'x':(33.45,15),'y':(12.20,400)}}}
    # market = {'x': 43.00, 'y':22.50}

    # for name, portfolio in portfolios.items():
    #     print(f"{name} {value(portfolio,market)}")

    # #problem 4
    # data = [[], [1],[1,2],[1,2,2,3],[0,2,4,6,8]]
    # for d in data:
    #     print(smooth(d))

    #problem 5
    # x = [7, -9, 5, 10, -9, 6, 9, 3, 3, 9]
    # print(msi(x))

    # #problem 6
    x_star = approx_root(f1,4)
    print(x_star, x_star**2 - 4*x_star - 7)

    x_star = approx_root(f0,.5)
    print(x_star, x_star - math.exp(-x_star))

    x_star = approx_root(f2,4)
    print(x_star, x_star**4 - 4*x_star - 7)

    x_star = approx_root(f3,3)
    print(x_star, x_star**5 - 3*(x_star**2) - 2)