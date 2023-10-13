# This is a linear sorting Algorithm

def countingSort(Arr):
    minNum = min(Arr)
    maxNum = max(Arr)
    countRange = (maxNum - minNum)+1
    count = [0] * countRange
    for i in Arr:
        count[i - minNum] += 1
    for i in range(1,len(count)):
        count[i] += count[i-1]
    new = [0]*len(Arr)
    for i in range(len(Arr)-1, -1, -1):
        count[Arr[i] - minNum] -= 1
        new[count[Arr[i]-minNum]] = Arr[i]
    return new
