# C200 / Spring 2025
# Lab 09
# Divya Rasania
# drasania

# binary sort
# [1,4,3,5,7,6]
# [1,4,3][5,7,6]
# [1,3,4][5,6,7]
# [1,2,3,4,5,6,7]
def binarySearch(array,x,low,high):
    # iterative
    # repeate until the pointers low and high meet each other
    while low <= high:
        mid = low + (high-low) // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binarySearchRec(array,x,low,high):
# FOR PRACTICE DURING LAB HOURS
# RECURSIVE BINARY SEARCH
    if low > high:
        return -1

    mid = low + (high - low) // 2

    if array[mid] == x:
        return mid
    elif array[mid] < x:
        return binarySearchRec(array, x, mid + 1, high)
    else:
        return binarySearchRec(array, x, low, mid - 1)

# bubble sort
# [4,7,2,9,1]
# [4,7,2,9,1]
# [4,2,7,9,1]
# [2,4,7,9,1]
# [1,2,4,7,9]
def bubbleSort(array):
    # loop over the indexes in the array
    for i in range(len(array)):

        # comparing elements to first for loop
        for j in range(0,len(array)-i -1):
            # ascending sorted list
            if array[j] > array[j+1]:

                # swapping the value if the elements are not in the intended order or "correct" order
                temp = array[j] #hold the value we want 
                array[j] = array[j+1]
                array[j+1] = temp

# insertion sort
# [2,4,1,6,3,9,8]
# [1,2,4,6,3,9,8]
# [1,2,4,6,3,9,8]
# [1,2,3,4,6,9,8]
# [1,2,3,4,6,9,8]
# [1,2,3,4,6,8,9]
def insertionSort(array):
    for step in range(1,len(array)):
        key = array[step]
        j = step - 1

        # capare key with each element on the left of it
        # until we run into a smaller value
        # decending: changing the key <array[j]
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j -1
        
        # place our key at after the element is just smaller 
        array[j+1] = key

# Tests
if __name__ == "__main__":
    # Binary Sort
    print("---BINARY SORT---")
    array = [3,4,5,6,7,8,9]
    x = 4
    print(f"Normal Binary Search: {binarySearch(array, x, 0, len(array)-1)}")
    print(f"Recurrsion Binary Search: {binarySearchRec(array, x, 0, len(array)-1)}")
    print(f"{'✅' if binarySearch(array, x, 0, len(array)-1) == binarySearchRec(array, x, 0, len(array)-1) else '❎'}")
    print()

    # Bubble Sort
    print("---BUBBLE SORT---")
    data = [-2,45,0,11,-9]
    print("pre-sorted: ",data)
    bubbleSort(data)
    print("post-sort: ", data)
    print()

    # Insertion Sort
    print("---INSERTION SORT---")
    data = [9,5,1,4,3]
    print("pre sort!: ", data)
    insertionSort(data)
    print("array is sorted using insertion sort!: ", data)
