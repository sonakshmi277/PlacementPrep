You are given an array nums consisting of positive integers.

You are also given an integer array queries of size m. For the ith query, you want to make all of the elements of nums equal to queries[i]. You can perform the following operation on the array any number of times:

Increase or decrease an element of the array by 1.
Return an array answer of size m where answer[i] is the minimum number of operations to make all elements of nums equal to queries[i].

Note that after each query the array is reset to its original state.

 

Example 1:

Input: nums = [3,1,6,8], queries = [1,5]
Output: [14,10]
Explanation: For the first query we can do the following operations:
- Decrease nums[0] 2 times, so that nums = [1,1,6,8].
- Decrease nums[2] 5 times, so that nums = [1,1,1,8].
- Decrease nums[3] 7 times, so that nums = [1,1,1,1].
So the total number of operations for the first query is 2 + 5 + 7 = 14.
For the second query we can do the following operations:
- Increase nums[0] 2 times, so that nums = [5,1,6,8].
- Increase nums[1] 4 times, so that nums = [5,5,6,8].
- Decrease nums[2] 1 time, so that nums = [5,5,5,8].
- Decrease nums[3] 3 times, so that nums = [5,5,5,5].
So the total number of operations for the second query is 2 + 4 + 1 + 3 = 10.

class Solution:
    def bin(self,nums,queries):
        low=0
        high=len(nums)-1
        while(low<=high):
                mid=(low+high)//2
                if(nums[mid]<=queries):
                    low=mid+1
                elif (nums[mid]>queries):
                    high=mid-1
        return high
    def prefix(self,nums):
        l=[0]*len(nums)
        l[0]=nums[0]
        for i in range(1,len(nums)):
            l[i]=l[i-1]+nums[i]
        return l
    def minOperations(self,nums,queries):
        nums.sort()
        p=self.prefix(nums)
        r=[]
        for i in range(len(queries)):
            d=self.bin(len(nums),nums,queries[i])
            low_ct=(d+1)
            high_ct=len(nums)-low_ct
            left_sum=p[d] if d>=0 else 0
            right_sum=p[-1]-left_sum
            ans = ((queries[i] * low_ct) - left_sum) + (right_sum - (queries[i] * high_ct))
            r.append(ans)
        return r


           
            

        