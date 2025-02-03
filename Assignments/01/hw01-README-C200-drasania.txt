C200 / Spring 2025
Homework Assignment 01
Divya Rasania
drasania

Task C:
(a) I was trying to put a string in int() which gave me invalid ValueError
(b) I was trying to concatenate string with None which gave me TypeError
(c) I was trying to divide a number by 0 which gave me ZeroDivisionError
=======================================================
Task D:
#1
Executing a script: A script is a file containing a sequence of Python instructions. We write this file in a text editor(IDLE→New File, Visual Studio Code), save it, and then execute it.
Interactive shell: The interactive shell is a command-line environment where you can type Python code one line at a time, and the interpreter immediately executes each line. Sometimes they are also called REPL (Read-Evaluate-Print Loop)

#2
def greet(person):
    print("Hello", person)

#3
import random; print(f"Random number: {random.randint(1,10)}")

#4
print("the same thing")

#5
if __name__ == "__main__": print("Hello")
=======================================================
Task F:
1. It will print nothing
2. I would wrap lines 5,6,10,11,15,16 in print()
=======================================================
Task G:
1.
17
<class 'int'>
'257'
<class 'str'>
2.7
<class 'float'>

2.
17
<class 'int'>
257
<class 'str'>
2.7
<class 'float'>
=======================================================
Task H:
1.
PREDICTIONS:
2.7
<class 'float'>
2
<class 'int'>

OUTPUT:
2.7
<class 'float'>
2.7
<class 'float'>

WHY?:
It was different from my prediction because the int converts the float but never stores it back into the variable and I didn't recognize that.

2. float
3. float
4. It never changes the type of variable because when its converted to int(line 4), it was never saved back to same variable
=======================================================
Task I:
1.
PREDICTIONS:
17
<class 'int'>
'17'
<class 'str'>

OUTPUT:
17
<class 'int'>
17
<class 'str'>

2. int
3. str
4. The variable did change type in line 4 because it was stored back in the varible after casting to string
=======================================================
Task J:
1.
PREDICTIONS:
'257'
<class 'str'>
257.0
<class 'float'>

OUTPUT:
257
<class 'str'>
257.0
<class 'float'>

2. str
3. float
4. Technically the variable never changed its type because when the value was casted to float in line 4, the result was never saved in the same variable.
=======================================================
Task K:
1. int
2. int
3. int (If the string has only numbers inside. Otherwise it will throw a error.)
4. float
5. float
6. float (If the string has only numbers inside. Otherwise it will throw a error.)
7. str
8. str
9. str
10. int
11. float
12. error 
13. float
14. str
15. int
16. float
17. str
18. error
19. float
20. int
21. int
22. float