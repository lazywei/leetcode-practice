# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from lc import *

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        result = {}

        queue = [(root, 1)]
        while queue:
            node, level = queue[0]
            queue = queue[1:]

            if not level in result:
                result[level] = []
            result[level].append(node.val)

            if node.left is not None:
                queue.append((node.left, level+1))
            if node.right is not None:
                queue.append((node.right, level+1))

        return list(result.values())

s = Solution()
trees = getTrees()
print s.levelOrder(trees[0])
