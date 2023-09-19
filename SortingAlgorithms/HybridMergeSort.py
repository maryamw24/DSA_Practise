
#----------------------- Hybrid Merge Sort ------------------#
#
# Steps involved:
# - First the array is divided into the smaller parts untill the size of array become 
#   equal to threshold value.
# - When it becomes equal a particular condition is satisfied and the part of the array 
#   sent to the insertion sort function which then performs sorting
# - Then at last all the parts are being connected by merge function and the resulting
#   array will be sorted.

# Code 
def insertionSort(Arr, start, end):
    for i in range(start+1, end):
        current = Arr[i]
        j = i - 1
        while (j >= start and current < Arr[j]):
            Arr[j+1] = Arr[j]
            j -= 1
        Arr[j+1] = current


def hybridmergeSort(Arr, start, end, t):
    mid = (start + end )//2 
    if(end- start)+1 >  t:
        hybridmergeSort(Arr, start, mid,t)
        hybridmergeSort(Arr, mid+1,end,t)
       
    else:
       insertionSort(Arr, start, end)
    Merge(Arr,start, mid, end)


def Merge(Arr,start,mid,end):
    L = Arr[start:mid+1]
    R = Arr[mid+1:end+1]
    i = 0
    j = 0
    k = start
    while i < len(L) and j < len(R):
        if(L[i]< R[j]): 
            Arr[k] = L[i]
            i+=1
        else: 
            Arr[k]=R[j]
            j+=1
        k+=1

    while i < len(L):
        Arr[k] = L[i]
        i+=1
        k+=1
    while j < len(R):
        Arr[k] = R[j] 
        j+=1
        k+=1
