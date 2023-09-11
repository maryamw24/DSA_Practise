#===========================  Intermediate Problems ================================#
#
#----------------------------- Reverse a String ------------------------------------#
def ReverseString(s):
    if len(s) == 1: return s
    else:
        return ReverseString(s[1:])+s[0]
print(ReverseString("mary"))

#----------------------------- Find first and Last Occurance -----------------------#
first = -1
last = -1
def findOccurrance(s,i,e):
    global first,last
    if i == len(s):
        print(first)
        print(last)
        return 
    else:
         if(s[i] == e):
            if(first == -1): first = i
            else: last = i
    findOccurrance(s,i+1,e)
findOccurrance("bddaanadnas",0,'a')

#------------------------- Checking if the Array id strictly sorted------------------#
def isSorted(arr, i):
    if i == len(arr)-1:return True
    else:
        if(arr[i] < arr[i+1]): return isSorted(arr, i+1)
        else: return False
print(isSorted([1,2,1,4,5], 0))