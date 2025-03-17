Given an array of integers arr[] representing inorder traversal of elements of a binary tree. Return true if the given inorder traversal can be of a valid Binary Search Tree.

Note - In a valid Binary Search Tree all keys are unique.

Examples :

Input: arr[] = [8, 14, 45, 64, 100]
Output: True

class Solution:
    def isBSTTraversal(self, arr):
        s=list(dict.fromkeys(arr))
        l=sorted(s)
        if(len(s)!=len(arr)  or   (l!=s)):
            return False
        return True