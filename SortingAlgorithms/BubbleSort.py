#=========================== Sorting Algorithms =============================#

#   ----------------------    Bubble Sort     ----------------------
# Steps involved
# - Repeatedly pass through the array
# - Swaps adjacent elements that are out of order

# Time Complexity : n^2

# Code implemented with the wole array sorting
def BubbbleSort(Arr):
    n = len(Arr)
    for i in range(n-1):
        for j in range(n-1-i):
            temp = Arr[j]
            if(Arr[j]> Arr[j+1]):
                Arr[j] = Arr[j+1]
                Arr[j+1] = temp
    return Arr

 
# Code implemented with start and end indexes to sort a part of that array
def BubbleSort(Arr, start, end):
   for i in range(start, end+1):
       for j in range(start,(start+end)-i):
           temp = Arr[j]
           if(Arr[j]> Arr[j+1]):
               Arr[j] = Arr[j+1]
               Arr[j+1] = temp
   return Arr