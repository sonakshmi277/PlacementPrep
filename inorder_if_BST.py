# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root,arr):
            if not root:
                return
            if root.left:
                dfs(root.left,arr)
            arr.append(root.val)
            if root.right:
                dfs(root.right,arr)
        arr=[]
        dfs(root,arr)
        r=0
        for i in range(1,len(arr)):
            if(arr[i-1]>=arr[i]):
                return False
        return True
                
            
        