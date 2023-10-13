# This is a linear sorting ALgorithm
import math

def insertionSort(Arr):
    for i in range(1,len(Arr)):
        key = Arr[i]
        j = i - 1
        while(j >= 0 and key < Arr[j]):
            Arr[j+1]= Arr[j]
            j -=1
        Arr[j+1] = key


def bucketSort(Arr):
    n = len(Arr)
    buckets = [[] for _ in range(n)]

    for i in Arr:
        index = math.floor(i * n)
        buckets[index].append(i)
    print(buckets)
    for bucket in buckets:
        insertionSort(bucket)
    ans = [bucket[i] for bucket in buckets for i in range (len(bucket))]
    return ans