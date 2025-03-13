# C200 / Spring 2025
# Lab 08
# Divya Rasania
# drasania

import os

def getCurrentDirectory():
    """
    This uses a command built into the python module `os` 
    that shows the current working directory. 

    Returns:
        A string that shows the current working directory 
        (Where the program is being executed at)
    """
    return os.getcwd()

def readingEx1():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    with open(f"{getCurrentDirectory()}\\blank.txt", "r") as blank_txt:
        contents = blank_txt.read()

    # return contents

def readingEx2():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    with open(f"{getCurrentDirectory()}\\blank.txt", "r") as blank_txt:
        contents = blank_txt.readlines()

    # return contents

def writeEx1():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice writing files
    """
    letters = ["a", "b", "c", "d", "e"]
    with open(f"{getCurrentDirectory()}\\letters.txt", "w") as letters_txt:
        for letter in letters:
            letters_txt.write(letter)

def writeEx2():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice writing files
    """
    with open(f"{getCurrentDirectory()}\\letters.txt", "a") as letters_txt:
        for _ in range(4):
            letters_txt.write("\nfghij")

def FileIO_example(filePath, newFile): 
    '''
    Given a file path, we want to open the file, read each line and count
    the number of vocabs in each line. We will write to
    the newFile the lines that have more than 5 vocabs and clean them up
    (use strip). You are provided the path to the file we want to write.

    Return number of all lines that has less than or equal to 5 vocabs.
    '''
    with open(filePath, "r") as read_file:
        contents = read_file.readlines()

    count = 0
    for line in contents:
        words = line.strip().split(" ")
        if len(words) >= 5:
            new_line = ""
            for word in words:
                new_line += f"{word} "
        else:
            count += 1
                
    with open(newFile, "a") as write_file:
        write_file.write(new_line + "\n")

    return count
            
if __name__ == "__main__":
    print()
    print("Examples of Reading")
    print("Our current working directory: " + getCurrentDirectory())
    print()
    print("Reading")
    readex1 = readingEx1()
    print("~"*30)
    print(readex1, end="") # end= removes the \n automatically added
    print("*EOF*")
    print("-" * 20)
    
    readex2 = readingEx2()
    print("~"*30)
    print(readex2, end="") # end= removes the \n automatically added
    print("*EOF*")
    print("-" * 20)
    print()

    print("Writing")
    print("-" * 20)
    writeEx1()
    writeEx2()
    print()
    print("Strip Lab Result: " + str(FileIO_example(f"{getCurrentDirectory()}\\testing.data", f"{getCurrentDirectory()}\\clean.txt")))

    
