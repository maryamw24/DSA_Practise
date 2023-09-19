#=========================== Sorting Algorithms =============================#

#   ----------------------     Selection Sort     ----------------------
# Steps involved
# - Find the smallest element in the array
# - Exchange it with the element in the first position
# - Find the second smallest element and exchange it with the element in the second position
# - continue untill the array is sorted

# Time Complexity : n^2 

# Code to sort the whole array
def SelectionSort(Arr):
    for i in range(len(Arr)-1):
        minimum = i
        for j in range(i+1,len(Arr)):
            if Arr[j]< Arr[minimum]: minimum = j
        temp = Arr[i]
        Arr[i] = Arr[minimum]
        Arr[minimum] = temp
    return Arr

# Code implemented with start and end indexes to sort a part of that array
def SelectionSort(Arr,start,end):
    print(len(Arr))
    for i in range(start, end):
        minimum = i
        for j in range(i+1,end+1):
            if Arr[j]< Arr[minimum]: minimum = j
        temp = Arr[i]
        Arr[i] = Arr[minimum]
        Arr[minimum] = temp
    return Arr
