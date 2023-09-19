import time 
import funcs as f

#----------------------------- Problem 3
def MergeSort(Arr, start, end):
    if start<end:
        mid = (start + end )//2
        MergeSort(Arr, start, mid)
        MergeSort(Arr, mid+1,end)
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