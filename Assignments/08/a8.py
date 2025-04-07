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
    pass
        
def get_child(name,data):
    return [child for parent,child in data if parent == name]

def has_children(name,data):
    pass

def get_parent(name,data):
    pass


def siblings(name1,name2,data):
    pass

def grandparent(name1,name2,data):
    pass

def get_all(data):
    pass

def cousins(name1,name2,data):
    pass

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
    pass

def get_DNA(path, filename):
    pass  

def translate(DNA_d, thedict):
    pass


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

def radix_decimal (lst):
    pass

########################
# PROBLEM 4
########################
def kns(lst, k = 0):
    pass


########################
# PROBLEM 5
########################
def get_fish_data(path,name):
    pass

#INPUT two lists X values and Y values of data
#RETURN a polynomial of degree three
def make_function(X,Y,degree):
    pass


########################
# PROBLEM 6
########################
def derivative(f, epsilon):
    pass
    
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
    # path = "../assignment-08/" 
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
    
    # aa_d = get_amino_acids("write the path here", fn1)
    # DNA_d = get_DNA("write the path here", fn2)
    # protein = translate(DNA_d)

    # # print("Dictionary")
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

    # X7,Y7 = get_fish_data("write the path here", fish_data.txt)
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
    