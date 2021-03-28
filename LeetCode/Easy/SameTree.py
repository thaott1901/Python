def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    if p == None and q == None:
        return True
    elif p == None or q == None:
        return False
    left = self.isSameTree(p.left, q.left)
    right = self.isSameTree(p.right, q.right)
    if left and right and p.val == q.val:
        return True
    return False