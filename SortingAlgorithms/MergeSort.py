#------------------------------- Merge Sort ----------------------------#
#
# Steps
# - We have to use the divide and conquer technique.
# - First we have to divide the array into left and right arrays untill only single unit is left in the array.
# - then we will merfe then arrays also applying the sorting algoritm.

# Code
def mergeSort(Arr):
    n = len(Arr)
    if(n <= 1):
        return Arr
    else:
        Left = mergeSort(Arr[0:n//2])
        Right = mergeSort(Arr[n//2: n])
        return Merge(Right, Left)

def Merge(L,R):
    A = []
    i = 0
    j = 0
    k = 0
    while i < len(L) and j < len(R):
        if(L[i]< R[j]): 
            A.append( L[i])
            i+=1
        else: 
            A.append(R[j])
            j+=1

    while i < len(L):
        A.append(L[i])
        i+=1
    while j < len(R):
        A.append(R[j])
        j+=1
    return A

print(mergeSort([2,4,1,3,6,5,0,8]))
