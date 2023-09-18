#----------------------------- Merge Sort --------------------------#

# - This algorithm sorts the indexes of array we provide to be sortd.

# Code 
def mergeSort(Arr, start, end):
    if start<end:
        mid = (start + end )//2
        mergeSort(Arr, start, mid)
        mergeSort(Arr, mid+1,end)
        Merge(Arr,start, mid, end)
    return Arr

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


#print(mergeSort([2,4,1,3,6,5,0,8],0,8))