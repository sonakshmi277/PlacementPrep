from collections import defaultdict, deque

class Solution:
    def verticalTraversal(self, node):
        d = defaultdict(list)
        q = deque([(node, 0, 0)])  
        while q:
            qlen = len(q)
            for _ in range(qlen):
                node, row, col = q.popleft()
                if node:
                    d[col].append((row, node.val)) 
                    if node.left:
                        q.append((node.left, row + 1, col - 1))
                    if node.right:
                        q.append((node.right, row + 1, col + 1))
        sorted_columns = sorted(d.keys())  
        result = []
        for col in sorted_columns:
            d[col].sort(key=lambda x: (x[0], x[1]))  # Sort by row first, then node value
            result.append([val for _, val in d[col]])  # Extract values

        return result


    