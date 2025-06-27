#You are given an integer array of N integers. Your task is to find and return an integer value representing the count of 
#elements in the array where the count of set bits is equal to a given number X.

#Note: A set bit refers to the value 1 of any bit for a number in its binary representation

#Input Specification:

#Input 1: An integer array of N elements.
#Input 2: An integer value N. representing the length of the array. 
#Input3: An integer value X. representing the target count of set bits.

#Output Specification:
#Return an integer value representing the count of elements in the array where the count of set bits is equal to a given number X.

#Example 1:
#input1 : [2, 3, 4, 5, 7, 12]
#input2 : 6
#input3: 2


arr = list(map(int, input().split()))
l=int(input())
bit_ct=int(input())
pw=0
ans=-1
for i in range(l):
    m=arr[i]
    ct=0
    while m:
        m&=(m-1)
        ct+=1
    if(ct==bit_ct):
        ans=arr[i]
        break
print(ans)
    
