class Tree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def preOrder(root):
    def dfs(root,ans):
        if not root:
            return
        ans.append(root.val)
        dfs(root.left,ans)
        dfs(root.right,ans)
    ans=[]
    dfs(root,ans)
    print(ans)
root=Tree(1)
root.left=Tree(2)
root.right=Tree(3)
root.right.left=Tree(4)
root.right.right=Tree(5)
preOrder(root)