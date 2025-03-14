import math

############
# PROBLEM 1
############
def s(n):
    if n == 0:
        return 0
    else:
        return s(n - 1) + n

ds1 = {}
def s_memo(n):
    """
    Calculate the sum of integers from 0 to n using memoization.
    
    Args:
        n (int): The upper limit of the sum
        
    Returns:
        int: The sum of integers from 0 to n
    """
    if n in ds1:
        return ds1[n]
    
    if n == 0:
        ds1[0] = 0
        return 0
    else:
        result = s_memo(n - 1) + n
        ds1[n] = result
        return result

def p(n):
    if n == 0:
        return 10000
    else:
        return p(n - 1) + (0.02 * p(n - 1))

def p_tail(n, acc=10000):
    """
    Calculate the compound growth of an initial value 10000 with 2% growth rate
    for n periods using tail recursion.
    
    Args:
        n (int): Number of periods
        acc (float): Accumulated value, defaults to 10000
        
    Returns:
        float: The value after n periods of growth
    """
    if n == 0:
        return acc
    else:
        return p_tail(n - 1, acc + 0.02 * acc)

def c(n):
    if n == 1:
        return 9
    else:
        return (9 * c(n - 1)) + (10 ** (n - 1)) - (c(n - 1))

def c_tail(n, acc1=9, i=1):
    """
    Calculate the function c(n) using tail recursion.
    
    Args:
        n (int): Input value
        acc1 (int): Current function value, defaults to 9 (c(1))
        i (int): Current index, defaults to 1
        
    Returns:
        int: The calculated value of c(n)
    """
    if i == n:
        return acc1
    else:
        next_i = i + 1
        next_acc = (9 * acc1) + (10 ** i) - acc1
        return c_tail(n, next_acc, next_i)

def c_while(n):
    while n != 1:
        return (9 * c(n - 1)) + (10 ** (n - 1)) - (c(n - 1))

    return 9 
    
############
# PROBLEM 2
############
def m(lst):
    """
    Build a pyramid of numbers according to the defined recursion.
    
    Args:
        lst (list): Input list of numbers
        
    Returns:
        list: A pyramid of numbers built according to the recursion rules
    """
    if len(lst) == 1:
        return []
    elif len(lst) == 2:
        return [[lst[0] + lst[1]]]
    else:
        next_level = [lst[i] + lst[i+1] for i in range(len(lst)-1)]
        result = m(next_level)
        result.append(next_level)
        
        return result

############
# PROBLEM 3
############
def d_1(x,y):
    """
    Calculates the greatest common divisor (GCD) of two numbers.
    
    Args:
        x (int): First integer
        y (int): Second integer
        
    Returns:
        int: The greatest common divisor of x and y
    """
    if x > 1:
        a = min(x, y)
        b = max(x, y)
        return d_1(b % a, a)
    elif x == 1:
        return x
    elif x == 0:
        return y

def e_1(x,y):
    """
    Calculates the least common multiple (LCM) of two numbers.
    
    Args:
        x (int): First integer
        y (int): Second integer
        
    Returns:
        int: The least common multiple of x and y
    """
    if d_1(x, y) == 1:
        return x * y
    else:
        z = d_1(x, y)
        return z * e_1(x // z, y // z)

############
# PROBLEM 4
############
def dollars(x):
    """
    Converts a dollar amount into the minimum number of quarters, dimes, nickels, and pennies.
    
    Args:
        x (float): Dollar amount to be converted
        
    Returns:
        list: A list containing the count of [quarters, dimes, nickels, pennies]
    """
    cents = round(x * 100)
    
    quarters = cents // 25
    cents %= 25
    
    dimes = cents // 10
    cents %= 10
    
    nickels = cents // 5
    cents %= 5
    
    pennies = cents
    
    return [quarters, dimes, nickels, pennies]

############
# PROBLEM 5
############
def D(f):
    """
    Returns the derivative function of the input function f.
    
    Args:
        f (function): The function to differentiate
        
    Returns:
        function: The derivative function of f
    """
    h = 0.00001
    return lambda x: (f(x + h) - f(x - h)) / (2 * h)

def newton(f, x, tau):
    """
    Implements the Newton-Raphson method to find a root of function f.
    
    Args:
        f (function): The function whose root is to be found
        x (float): The initial guess
        tau (float): The threshold for convergence
        
    Returns:
        float: An approximation of a root of f
    """
    fx = f(x)
    if abs(fx) <= tau:
        return x
    
    df = D(f)
    dfx = df(x)
    if abs(dfx) < 1e-10:
        return x
    
    x_next = x - fx / dfx
    return newton(f, x_next, tau)

############
# PROBLEM 6
############
def prime(p):
    """
    Checks if a number is prime.

    Args:
        p (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if (p % 2 == 0 or p % 3 == 0) and not (p == 2 or p == 3):
        return False

    count = 5
    while count * count <= p:
        if p % count == 0 or p % (count + 2) == 0:
            return False
        count += 6

    return True

if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You **do not** have to put anything here
    """

    # Problem 1
    # for i in range(4):
    #     print(f"n = {i}")
    #     print(f"s(n) = {s(i)} s_memo(n) = {s_memo(i)}")
    #     print(f"p(n) = {p(i)} p_tail(n) = {p_tail(i)}")
    # print()
    # for i in range(1,5):
    #     print(f"n = {i}")
    #     print(f"c(n) = {c(i)} c_tail(n) = {c_tail(i)} c_while(n) = {c_while(i)}")

    # Problem 2
    # x = [[1,2,3,4,5], [1], [3,4], [5,10,22], [1,2,3,4,5,6]]
    # for i in x:
    #     print(m(i))

    # Problem 3
    # data = [[15,25], [6,7], [1,1], [1,2],[0,4], [210, 2310]]
    # for i in data:
    #     print(e_1(*i))

    # Problem 4
    # data5 = [2.24,1.19,4.16,1.01,1.10,2.00]
    # for i in data5:
    #       print(dollars(i))

    # Problem 5
    # p1 = [[lambda x:x**2 - 2, 100],[lambda x:x**6-x-1,1.5],
    #       [lambda x:x**3-(100*(x**2))-x + 100,0]]
    # tau = 0.0001

    # for f,g in p1:
    #     root = newton(f,g,tau)
    #     print(root,f(root))

    # Problem 6
    # ps = []
    # for p in range(2,100):
    #     if prime(p):
    #         ps.append(p)
    # print(ps)

    print()