#=========================== Sorting Algorithms =============================#

#   ----------------------     Selection Sort     ----------------------
# Steps involved
# - Find the smallest element in the array
# - Exchange it with the element in the first position
# - Find the second smallest element and exchange it with the element in the second position
# - continue untill the array is sorted

# Code
def SelectionSort(Arr):
    for i in range(len(Arr)-1):
        minimum = i
        for j in range(i+1,len(Arr)):
            if Arr[j]< Arr[minimum]: minimum = j
        temp = Arr[i]
        Arr[i] = Arr[minimum]
        Arr[minimum] = temp
    return Arr
print(SelectionSort([3,5,7,0,8,6,4,3,-1]))

        

                

