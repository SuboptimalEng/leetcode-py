# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        sol = []
        self.helper(root, sol)
        return sol

    def helper(self, root, sol):
        if root is None:
            return
        self.helper(root.left, sol)
        sol.append(root.val)
        self.helper(root.right, sol)
