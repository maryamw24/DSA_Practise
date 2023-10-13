# This is a linear sorting Algorithm



def radixSort(Arr):
    maximum = max(Arr)
    placeValue = 1
    a = Arr.copy()
    while maximum > 0:
        a = countSort(a, placeValue)
        placeValue *= 10
        maximum //= 10
    return a


def countSort(Arr, placeValue):
    minNum = 0
    maxNum = 9
    countRange = (maxNum - minNum) + 1
    # print(countRange)
    count = [0] * countRange
    for i in Arr:
        digit = i // placeValue
        digit1 = digit % 10
        count[digit1] += 1
    # print(count)
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    # print(count)
    new = [0] * len(Arr)
    for i in range(len(Arr) - 1, -1, -1):
        digit = Arr[i] // placeValue
        digit1 = digit % 10
        count[digit1] -= 1
        new[count[digit1]] = Arr[i]
    # print(new)
    return new