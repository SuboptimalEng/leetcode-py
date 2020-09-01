# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, float("-inf"), float("inf"))

    def helper(self, root, minValue, maxValue):
        if root is None:
            return True
        if root.val <= minValue or root.val >= maxValue:
            return False
        validLeft = self.helper(root.left, minValue, root.val)
        validRight = self.helper(root.right, root.val, maxValue)
        return validLeft and validRight


