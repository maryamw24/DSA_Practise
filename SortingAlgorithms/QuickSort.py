#------------------------- Quick Sort Algorithm----------------

def quickSort(Arr, low, high):
    if high > low:
        pivotIndex = partition(Arr, low, high)
        quickSort(Arr, low, pivotIndex-1)
        quickSort(Arr, pivotIndex+1,high)

def partition(Arr, low, high):
    pivot = Arr[high]
    i = low -1
    for j in range (low, high):
        if Arr[j] < pivot:
            i += 1
            Arr[j], Arr[i] = Arr[i], Arr[j]
    i+=1
    Arr[i], Arr[high] = Arr[high], Arr[i]
    return i

Arr = [3,6,7,1,8,0]
quickSort(Arr, 0, 5)
print(Arr)