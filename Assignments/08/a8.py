import csv
import numpy as np
import matplotlib.pyplot as plt
import math

########################
# PROBLEM 1
########################
# CONSTRAINTS
# use csv reader
# All solutions must be in comprehension

def get_data(path, filename):
    """
    Given a path and filename, read the file and return a list of tuples.
    Each tuple contains a parent and child name.

    Args:
        path (str): The path to the file.
        filename (str): The name of the file.

    Returns:
        list: A list of tuples where each tuple contains a parent and child name.
    """
    with open(f"{path}/{filename}", "r") as family_txt:
        content_lst = family_txt.read().split("\n")
        return [item.split(",") for item in content_lst]

def get_child(name, data):
    """
    Given a name, return the children of that name.
    
    Args:
        name (str): The name of the parent.
        data (list): The family data.
    
    Returns:
        list: A list of children names.
    """
    return [child for parent, child in data if parent == name]

def has_children(name, data):
    """
    Given a name, return True if the name has children.

    Args:
        name (str): The name of the parent.
        data (list): The family data.

    Returns:
        bool: True if the name has children, False otherwise.
    """
    return bool(get_child(name, data))

def get_parent(name, data):
    """
    Given a name, return the parent of that name.

    Args:
        name (str): The name of the child.
        data (list): The family data.

    Returns:
        int: The parent name.
    """
    return [parent for parent, child in data if child == name]

def siblings(name1, name2, data):
    """
    Given two names, return True if they are siblings (i.e., share the same parent).

    Args:
        name1 (str): The first name.
        name2 (str): The second name.
        data (list): The family data.

    Returns:
        bool: True if the names are siblings, False otherwise.
    """
    parent1 = get_parent(name1, data)
    parent2 = get_parent(name2, data)
    return parent1 == parent2

path = "Assignments/08"
filename = "family.txt"
data_1 = get_data(path, filename)

def grandparent(name1, name2, data):
    """
    Given two names, return True if the first name is a grandparent of the second name.
    
    Args:
        name1 (str): The grandparent name.
        name2 (str): The grandchild name.
        data (list): The family data.

    Returns:
        bool: True if the first name is a grandparent of the second name, False otherwise.
    """
    name2_parents = get_parent(name2, data)
    
    for parent in name2_parents:
        grandparents = get_parent(parent, data)
        if name1 in grandparents:
            return True
    
    return False

def get_all(data):
    """
    Given a list of tuples, return a list of all names in the data.

    Args:
        data (list): The family data.

    Returns:
        list: A list of all names.
    """
    return [k for k in [i for i, j in data] + [j for i, j in data]]

def cousins(name1, name2, data):
    """
    Given two names, return True if they are cousins (i.e., share the same grandparents).
    
    Args:
        name1 (str): The first name.
        name2 (str): The second name.
        data (list): The family data.
        
    Returns:
        bool: True if the names are cousins, False otherwise.
    """
    if name1 == name2:
        return False
    
    parents1 = get_parent(name1, data)
    parents2 = get_parent(name2, data)
    
    if not parents1 or not parents2:
        return False
    
    if any(p in parents2 for p in parents1):
        return False
    
    grandparents1 = set()
    grandparents2 = set()
    
    for parent in parents1:
        grandparents1.update(get_parent(parent, data))
    for parent in parents2:
        grandparents2.update(get_parent(parent, data))
    
    return bool(grandparents1 & grandparents2)

########################
# PROBLEM 2
########################
#the dictionary for the transation
aa_d = {}
#the list to store the contents of the FASTA file
DNA_d = []

# DO NOT CHANGE
actual = "PLHSPHPANFCVFSRD-IPYSEHLRRGALDPGRFRGPRSELSEIERARSRDLRRGPGPPGGEAAARRPLEAAGPLAGPRRRSGVAGRGGFQRGDGAVRGGPGAGARPVEEAGQQRRRLHDRGPGKVRQAGRPRPQGPSLPKPPGRASPTFLSQDLPGFPRHEDLLLPPGPEPRLLTSQSPRPEGGGRAEPRRGAPGRPTPRAVRAEPPARVPAASGPGQLPGERLPCWAPVPGRAPAGWVRGACGAGAGE-ALSARRSSWATACW-PSPGTTPETSAPRCRRRWTSS-ATLSRRWFPSTAELWVGGRGIPRRPSPCLSKASPRSSLLAVLSRGQDARGRR"

def get_amino_acids(path, filename):
    """
    Reads the amino_acids.txt file and constructs a dictionary mapping
    tuples of codons to [full name, abbreviation] of the amino acid.
    """
    with open(path + filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            name = parts[0]
            letter = parts[1]
            codons = tuple(parts[2].split(','))
            aa_d[codons] = [name, letter]
    return aa_d

def get_DNA(path, filename):
    """
    Reads the DNA.txt file (in FASTA format) and returns a list with the header
    and full DNA sequence with all line breaks and whitespace removed.
    """
    with open(path + filename, 'r') as file:
        lines = file.readlines()
        header = lines[0].strip()
        dna_sequence = ''.join(line.strip() for line in lines[1:])
    return [header, dna_sequence]

def translate(DNA_d, thedict):
    """
    Translates a DNA sequence into a protein string using the provided codon dictionary.
    """
    dna = DNA_d[1]
    protein = ""
    i = 0
    while i + 2 < len(dna):  # Ensure there's a full codon (3 bases)
        codon = dna[i:i+3]
        matched = False
        for codon_set, (name, letter) in thedict.items():
            if codon in codon_set:
                protein += letter
                matched = True
                break
        if not matched:
            pass
        i += 3
    return protein

########################
# PROBLEM 3
########################
# DO NOT CHANGE, we have already completed this function for you.
# input list of numbers as strings
# output sorted as numbers using radix sort
def radix (lst,digit_index = 0):
    """
    Given a list of integers (as strings), return them sorted using radix sort.

    List, Integer -> List
    """
    if lst:
        cluster = [[] for _ in range(10)]
        for number in lst:
            index = int(number[-(digit_index + 1)])
            cluster[index] += [number]
       
        sorted, unsorted = [],[]
        for block in cluster:
            for number in block:
                if len(number) > digit_index + 1:
                    unsorted.append(number)
                else:
                    sorted.append(number)
        return sorted + radix(unsorted, digit_index + 1) 
    else:
        return []

def radix_decimal(lst):
    """
    Given a list of decimal numbers (as strings), return them sorted using radix sort.
    
    Args:
        lst (list): List of decimal numbers as strings (e.g. [".301", ".101", ".20"])
        
    Returns:
        list: Sorted list of decimal numbers as strings, without trailing zeros
    """
    max_length = max(len(num.replace('.', '')) for num in lst)
    padded = [num.replace('.', '').ljust(max_length, '0') for num in lst]
    
    sorted_nums = radix(padded)
    
    result = []
    for num in sorted_nums:
        decimal = '.' + num
        decimal = decimal.rstrip('0')
        if decimal[-1] == '.':
            decimal += '0'
        result.append(decimal)
    
    return result

########################
# PROBLEM 4
########################
def kns(lst, k=0):
    """
    Given a list of integers and a target sum k, return a list of tuples containing
    all possible subset sums and their corresponding subsets.
    
    Args:
        lst (list): List of integers
        k (int): Target sum, defaults to 0
        
    Returns:
        list: List of tuples (sum, subset) for all possible combinations
    """
    n = len(lst)
    result = []
    
    for i in range(1, 1 << n):
        subset = []
        subset_sum = 0
        for j in range(n):
            if i & (1 << j):
                subset.append(lst[j])
                subset_sum += lst[j]
        result.append((subset_sum, subset))
    
    result.sort(key=lambda x: (x[0], len(x[1])))
    
    return result

########################
# PROBLEM 5
########################
def get_fish_data(path, name):
    """
    Read fish measurement data from a CSV file.
    
    Args:
        path (str): Path to the file
        name (str): Name of the file containing fish data
        
    Returns:
        list: Two lists containing X values (age) and Y values (length)
    """
    X, Y = [], []
    with open(f"{path}/{name}", 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            if len(row) >= 2:
                X.append(float(row[0]))
                Y.append(float(row[1]))
    return X, Y

#INPUT two lists X values and Y values of data
#RETURN a polynomial of degree three
def make_function(X, Y, degree):
    """
    Create a polynomial function of specified degree that fits the data points.
    
    Args:
        X (list): List of x-coordinates (age)
        Y (list): List of y-coordinates (length)
        degree (int): Degree of the polynomial
        
    Returns:
        function: A polynomial function that fits the data
    """
    X = np.array(X)
    Y = np.array(Y)
    
    coefficients = np.polyfit(X, Y, degree)
    
    return np.poly1d(coefficients)

########################
# PROBLEM 6
########################
def derivative(f, epsilon):
    """
    Returns a lambda function that approximates the derivative of f using
    the symmetric difference quotient formula.
    
    Args:
        f (function): The function to differentiate
        epsilon (float): Small value for numerical approximation
        
    Returns:
        function: Lambda function that computes derivative at a point
    """
    return lambda x: (f(x + epsilon) - f(x - epsilon)) / (2 * epsilon)
    
# DO NOT CHANGE
def f(x):
    return x**2 - 3*x

if __name__ == "__main__":
    """
    WARNING: Since we are working with files, make sure you are setting the 
    correct path to the files you are working with. 

    WARNING: Ensure that you comment out any plotting code before submitting to the Autograder
    """

    # problem 1
    # path = "Assignments/08"
    # filename = "family.txt"
    # data_1 = get_data(path, filename)
    # print(data_1)
    # print(has_children('0', data_1)) #true
    # print(has_children('7', data_1)) #false
    # print(get_child('6', data_1))
    # print(get_parent('g', data_1))
    # print(siblings('7','A', data_1)) #true
    # print(siblings('2','7', data_1)) #false
    # print(grandparent('0','3', data_1)) #true
    # print(grandparent('0','7', data_1)) #false
    # print(get_all(data_1))
    # print(cousins('3','6', data_1)) #true
    # print(cousins('3','5', data_1)) #false

    # problem 2
    # Only when submitting to the Autograder, leave the path as blank string "", only provide the filename "DNA.txt" or "amino_acids.txt"
    # To test on your system, you may need to provide the path as well. We encourage some testing to figure it out. 
    # please remember that on Windows - the path use two back slashes \\, while on MAC and Linux the path use forward slash  /
        
    # fn1, fn2 = "amino_acids.txt", "DNA.txt"
    # print(fn1,fn2)
    
    # aa_d = get_amino_acids("Assignments/08", fn1)
    # DNA_d = get_DNA("Assignments/08", fn2)
    # protein = translate(DNA_d)

    # print("Dictionary")
    # print(aa_d)
    # print("FASTA file")
    # print(DNA_d)
    # print("Translations match:", str(protein == actual))

    # #should return "PLHS"    
    # print(translate(["nothing", "CCACTGCACTCA"], aa_d))

    # #should returns "D-"
    # print(translate(["nothing", "GACTAA"], aa_d))

    # problem 3
    # data21 = ["101","10","12","1000","99","1","5", '100', '120', '990', '310', '0', '301', '102', '654']
    # print(radix(data21))
    # data22 = [".301",".101",".20",".1",".12",".654",".99",".31",".309",]
    # print(radix_decimal(data22))
    # d_22 = data22[::]
    # d_22.sort()
    # print(d_22)

    # problem 4
    # lst = [1,2,3]
    # print(kns(lst,0))
    # print(kns(lst,3))
    # print(kns(lst,sum(lst)))
    # print(kns([1,2,1],2))

    # problem 5
    # Only when submitting to the Autograder, leave the path as blank string "", only provide the filename "fish_data.txt"
    # To test on your system, you may need to provide the path as well. We encourage some testing to figure it out. 
    # please remember that on Windows - the path use two back slashes \\, while on MAC and Linux the path use forward slash  /

    # X7,Y7 = get_fish_data("Assignments/08", "fish_data.txt")
    # data7 = [[i,j] for i,j in zip(X7,Y7)]
    # print(data7)

    # The following code is for drawing the plot. Please comment it out after testing your solution and before submitting to the Autograder. 
    # Also, comment out the import matplotlib at the top of this file.

    # plt.plot(X7,Y7,'ro')
    # xp7 = np.linspace(1,14,10)
    # degree = 3
    # p3 = make_function(X7,Y7,degree)
    # plt.plot(xp7,p3(xp7),'b')
    # plt.xlabel("Age (years)")
    # plt.ylabel("Length (inches)")
    # plt.title("Rock Bass Otolith")
    # plt.show()

    # problem 6
    # data = 3 
    # epsilon = 10e-8
    # print((derivative(f,epsilon)(data)))
    # f_prime = derivative((lambda x:x**2-3*x),epsilon)
    # print(f_prime(data))

    # uncomment to see the AI plot and your derivative in action!
    # Remember to comment out the following plotting code and also the import of matplotlib before submitting to the Autograder.
    # The following plotting code makes use of your derivative function.
    # N = 50
    # x = np.linspace(1,14,100)
    # gm = np.zeros(N)
    # r = np.zeros(N)
    # def mean(lst):
    #     s_ = 0
    #     N = len(lst)
    #     for i in range(N):
    #         s_ += lst[i]
    #     m_ = round(s_/N,2)
    #     return m_

    # def residuals(lst,m):
    #     s_ = 0
    #     N = len(lst)
    #     for i in range(N):
    #         s_ += (lst[i] - m)**2
    #     m_ = (1/2)*(s_/N)
    #     return m_
    # data = [1,1,2,6,10,12,13,14]

    # def update(w,data):
    #     eta = .2
    #     epsilon = 0.00001
    #     return w - eta*(derivative(lambda x:residuals(data,x),epsilon)(w))

    # m_ = mean(data)
    # fmean = 1
    # for i in range(N):
    #     gm[i] = fmean
    #     r[i] = residuals(data,fmean)
    #     # print(fmean,residuals(data,fmean))
    #     fmean = update(fmean,data)

    # print(gm[-1])
    # print(m_)
    # plt.plot(gm,r,'bo')
    # for i in range(1,N):
    #     plt.plot([gm[i-1],gm[i]],[r[i-1],r[i]],'b--')
    # plt.plot(m_,residuals(data,m_),'ro')
    # plt.xlabel("Possible means")
    # plt.ylabel("Error")
    # plt.title(f"Using AI to search for the best mean {gm[-1]}")
    # plt.show()

    pass
    