#You are required to implement the following Function def LargeSmallSum(arr). 

#The function accepts an integers arr of size ’length’ as its arguments you are required to return the sum of 
#second largest largest element from the even positions and second smallest from the odd position of given ‘arr’.

#Assumption:

#All array elements are unique
#Treat the 0th position as even

#Return 0 if array is empty
#Return 0, if array length is 3 or less than 3
#Example:-

#Input

#arr: 3 2 1 7 5 4

#Output: 7

#Explanation

#Second largest among even position elements(1 3 5) is 3
#Second largest among odd position element is 4
#Thus output is 3+4 = 7

#Sample Input - arr: 1 8 0 2 3 5 6

def LargeSmallSum(arr):
    el_even2=float('-inf')
    el_even1=float('-inf')
    el_odd2=float('-inf')
    el_odd1=float('-inf')
    for i in range(0,len(arr)):
        if(i%2==0):
            if(arr[i]>el_even1):
                el_even2=el_even1
                el_even1=arr[i]
            elif(arr[i]>el_even2 and arr[i]!=el_even1):
                el_even2=arr[i]
        elif (i%2!=0):
            if(arr[i]>el_odd1):
                el_odd2=el_odd1
                el_odd1=arr[i]
            elif(arr[i]>el_odd2 and arr[i]!=el_odd1):
                el_odd2=arr[i]
    print(el_odd2+el_even2)


    
LargeSmallSum([3,2,1,7,5,4])