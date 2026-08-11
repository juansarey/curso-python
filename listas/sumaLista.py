def evenSquareSum():
    #write code here
    l1 = [x*x for x in range(0,21) if(x%2)==0]
    return sum(l1)

print("Sum of squares of even numbers: ", evenSquareSum())



def getSquare():
    ##Write your code here
    l1 = [x*x for x in range(0,21) if ((x%3)!=0) & ((x%2)==0)] ##Create the list here
    return l1

print("Squares of even numbers not divisible by 3: ", getSquare())