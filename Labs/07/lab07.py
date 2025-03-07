def while_factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def tail_factorial(n, a=1):
    if n == 0: 
        return a
    else:
        return tail_factorial(n-1, a=a*n)

d = {}
def memo_factorial(n):
    if n not in d.keys():
        if n == 1:
            d[n] = 1
        else:
            d[n] = n * memo_factorial(n-1)
    return d[n]

if __name__ == "__main__":
    print("Factorial Practice")
    indicies = [1, 2, 3,  4,   5,   6,      10]
    answers  = [1, 2, 6, 24, 120, 720, 3628800]
    functions = [while_factorial, factorial, tail_factorial, memo_factorial]

    for func in functions:
        if func(indicies[0]) != None:
            print("="*5, "Testing: "+func.__name__+"()", "="*5)
            print("Our Inputs:", indicies)
            print("Your Outputs:")
            for i in range(len(indicies)):
                result = func(indicies[i])
                correct = int(bool(result == answers[i]))
                print("  {0}({1}) == {2} \t{3}".format(func.__name__, indicies[i], result, ("WRONG", "RIGHT")[correct]))
            print("\n\n")
