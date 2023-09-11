#=========================== Practise for Recursion====================#
#
#-------------------------- Print numbers from 5 to 1 -----------------#
def PrintNumbers(n):
    if(n == 0): return 0 # Base Case
    else:
        print(n)
        PrintNumbers(n-1)
PrintNumbers(5)

#-------------------------- Print numbers from 1 to 5 -----------------#
def Printnumbers(num):
    if(num == 6): return # Base Case
    else:
        print(num)
        Printnumbers(num+1)
Printnumbers(1)

#---------------------- Print sum of numbers from 1 to 5 ---------------#
def SumOfNumbers(num):
    if(num == 0):return 0 # Base Case
    else:
        return (num + SumOfNumbers(num-1))
print(SumOfNumbers(5))

#-------------------------- Print Factorial of number ------------------#
def FactorialOfNumber(num):
    if(num == 0): return 1 # Base Case
    else:
        return (num * FactorialOfNumber(num-1))
print(FactorialOfNumber(0))

#----------------------------- Fibonacci Series  -----------------------#
def PrintFibonacciSeries(a,b,n):
    if(n == 0): return  # Base Case
    else:
        c = a + b
        print(c)
        PrintFibonacciSeries(b,c,n-1)
print(0)
print(1)
PrintFibonacciSeries(0,1,5)

#-------------------------- n power of a number -----------------#
#      Stack hieght n
def CalculatePower(x,n):
    if(n == 0): # Base Case1
        return 1
    if x == 0 :# Base Case2
        return 0
    else:
        return x* CalculatePower(x,n-1)
    
#      Stack height logn
def CalculatePower(x,n):
    if(n == 0): # Base Case1
        return 1
    if x == 0 :# Base Case2
        return 0
    if(n % 2 == 0): return CalculatePower(x,n//2) * CalculatePower(x, n//2)
    else : return CalculatePower(x,n//2) * CalculatePower(x, n/CalculatePower//2) * x
print(CalculatePower(2,3))
