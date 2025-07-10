class Solution:

    def findElement(self, arr):
        n=len(arr)
        if n<=2:
            return -1
        left=[0]*n
        left[0]=arr[0]
        right=[0]*n
        right[-1]=arr[-1]
        for i in range(1,n):
            left[i]=max(left[i-1],arr[i])
        for j in range(n-2,-1,-1):
            right[j]=min(right[j+1],arr[j])
        for k in range(1,n-1):
            if(left[k-1]<=arr[k] and arr[k]<=right[k+1]):
                return arr[k]
        return -1