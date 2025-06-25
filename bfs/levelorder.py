from collections import deque
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        q=deque()
        ans=[]
        q.append(root)
        while q:
            qlen=len(q)
            level=[]
            for i in range(qlen):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            ans.append(level)
                
        return ans






        