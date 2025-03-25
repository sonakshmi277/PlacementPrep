def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        st = []
        p = []
        cur = root
        while cur or st:
            if cur:
                st.append(cur)
                cur = cur.left
            else:
                temp = st[-1].right
                if not temp:
                    temp = st.pop()
                    p.append(temp.val)
                    while st and temp == st[-1].right:
                        temp = st.pop()
                        p.append(temp.val)
                else:
                    cur = temp
        return p
