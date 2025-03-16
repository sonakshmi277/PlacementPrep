#Write a program to find the sum of minimum absolute difference using python
def sumOfMinAbsDifferences(arr,n):
    # sort the given array
    arr.sort()
    
    sum = 0
         
    sum += abs(arr[0] - arr[1]);
         
    sum += abs(arr[n - 1] - arr[n - 2]);
         
    
    for i in range(1, n - 1):
        sum += min(abs(arr[i] - arr[i - 1]),
                  abs(arr[i] - arr[i + 1]))
             
    # required sum
    return sum
         
 
# Driver code
arr = [2, 5, 4, 3]
n = len(arr)
print( "Required Sum is", sumOfMinAbsDifferences(arr, n))