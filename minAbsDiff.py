Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
 

Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_diff = sys.maxsize
        arr.sort()
        res = []
        for i in range(len(arr)-1):

            diff = arr[i+1] - arr[i]

            if diff < min_diff:
                min_diff = diff
                res = [[arr[i],arr[i+1]]]
            elif diff == min_diff:
                res += [[arr[i],arr[i+1]]]
        return res