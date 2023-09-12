#=========================== Sorting Algorithms =============================#

#   ----------------------     Selection Sort     ----------------------
# Steps involved
# - Repeatedly pass through the array
# - Swaps adjacent elements that are out of order

# code
def BubbbleSort(Arr):
    n = len(Arr)
    for i in range(n-1):
        for j in range(0, n-1-i):
            temp = Arr[j]
            if(Arr[j]> Arr[j+1]):
                Arr[j] = Arr[j+1]
                Arr[j+1] = temp
    return Arr
print(BubbbleSort([4,2,6,-3,1,7]))
