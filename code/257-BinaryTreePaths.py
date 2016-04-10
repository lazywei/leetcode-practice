# Link: https://leetcode.com/problems/binary-tree-paths/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import lc

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]

        paths = self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)
        return list(map(lambda path: str(root.val) + "->" + path, paths))


s = Solution()
print s.binaryTreePaths(lc.buildTree([5,4,1,None,1,None,4,2,None,2,None]))
print s.binaryTreePaths(lc.buildTree([1, 2, 2, 3, 4, 4, 3]))
