# Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        queue = [(root, 1)]
        while queue:
            node, level = queue[0]
            queue = queue[1:]

            if self.isLeaf(node):
                return level

            if node.left is not None:
                queue.append((node.left, level+1))
            if node.right is not None:
                queue.append((node.right, level+1))


    def isLeaf(self, root):
        return root.left is None and root.right is None
