# Link: https://leetcode.com/problems/balanced-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from lc import *

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        if self.isBalanced(root.left) and self.isBalanced(root.right)\
           and abs(self.height(root.left) - self.height(root.right)) <= 1:
            return True
        else:
            return False

    def height(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        leftDepth = self.height(root.left)
        rightDepth = self.height(root.right)

        return max(leftDepth, rightDepth) + 1

s = Solution()
root = TreeNode(0)
root.left = TreeNode(1)
root.left.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(3)
root.left.left.right = TreeNode(4)
root.left.left.left = TreeNode(4)
root.left.left.left.left = TreeNode(4)

print s.isBalanced(root)
print s.isBalanced(root.right)
print s.isBalanced(root.left)
