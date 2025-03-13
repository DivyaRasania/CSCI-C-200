# C200 / Spring 2025
# Lab 08
# Divya Rasania
# drasania

def fibonacci(n):
    """
    Recursive function to return the nth number in the fibonacci sequence
    The fibonacci sequence is a series of numbers where each number is the sum of the two numbers before it (starting with 0, 1)
    So 0, 1, 1, 2, 3, 5, 8, 13...

    Input:
        n (integer >=0)
    
    Returns:
        int: nth number in fibonacci sequence
    """
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_tail(n, acc1 = 0, acc2 = 1):
    """
    Recursive function to return the nth number in the fibonacci sequence
    The fibonacci sequence is a series of numbers where each number is the sum of the two numbers before it (starting with 0, 1)
    So 0, 1, 1, 2, 3, 5, 8, 13...

    Input:
        n (integer >= 0)
    
    Returns:
        int: nth number in fibonacci sequence
    """
    if n == 0:
        return acc1
    if n == 1:
        return acc2
    return fibonacci_tail(n - 1, acc1 = acc2, acc2 = acc2 + acc1)

if __name__ == "__main__":
    #simple tests
    answers=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    print("~~~Testing recursive fibonacci~~~")
    for i in range(13):
        test=fibonacci(i)
        print(f"Your answer: {test} Correct Answer: {answers[i]} Same: {test==answers[i]}")

    print("\n~~~Testing tail recursive fibonacci~~~")
    for i in range(13):
        test=fibonacci_tail(i)
        print(f"Your answer: {test} Correct Answer: {answers[i]} Same: {test==answers[i]}")
