#=========================== Sorting Algorithms =============================#

#   ----------------------     Selection Sort     ----------------------
# Steps involved (Idea is like sorting a hand of playing cards)
# - Start with an empty left hand and the cards facing down on the table.
# - Remove one card at a time from the table, and insert it into the correct position in the left hand
#   * compare it with each of the cards already in the hand, from right to left
# - The cards held in the left hand are sorted
#   * these cards were originally the top cards of the pile on the table

# Time Complexity : n^2

# Code implemented to sort the whole array
def insertionSort(Arr):
    for i in range(1, len(Arr)):
        current = Arr[i]
        j = i-1
        while(j >= 0 and current < Arr[j]):
            Arr[j+1] = Arr[j]
            j -= 1
        Arr[j+1] = current
    return Arr

# Code implemented to sort the whole array
def InsertionSort(Arr, start, end):
    for i in range(start+1, end+1):
        current = Arr[i]
        j = i-1
        while (j >= start and current < Arr[j]):
            Arr[j,+1] = Arr[j]
            j -= 1
        Arr[j+1] = current
    return Arr
