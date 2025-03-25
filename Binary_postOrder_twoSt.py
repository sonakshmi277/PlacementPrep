class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postOrder=[]
        if root is None:
            return []
        st1=[]
        st2=[]
        st1.append(root)
        while st1:
            root=st1.pop()
            st2.append(root)
            if root.left:
                st1.append(root.left)
            if root.right:
                st1.append(root.right)
        while st2:
            postOrder.append(st2[-1].val)
            st2.pop()
        return postOrder
