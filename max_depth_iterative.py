from queue import Queue
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q=Queue()
        l=0
        if (root is None):
            return 0
        q.put(root)
        while not q.empty():
            n=q.qsize()
            for _ in range(n):
                front=q.get()
                if front.left is not None:
                    q.put(front.left)
                if front.right is not None:
                    q.put(front.right)
            l+=1
        return l

            
                

        

        