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

print(hybridmergeSort([2,4,6,5,0,-1,19,10,-10,12, 25, 16],0,12,4))