# Link: https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# In-Order: [3, 2, 4, 1, 4, 2, 3]
#
#   1
#  / \
# 2   2
#  \   \
#  3    3
# In-Order: [#, 2, 3, 1, #, 2, 3]
#
#     5
#    / \
#   4   1
#  / \ / \
#    1    4
#   / \  / \
#   2    2
# In-Order: [3, 2, #, 1, 2, 3, #]


import lc

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        return self.checkSym(root.left, root.right)

    def checkSym(self, left, right):
        if left is None:
            return right is None
        if right is None:
            return left is None

        return (left.val == right.val) and self.checkSym(left.left, right.right) and self.checkSym(left.right, right.left)


    # def inOrder(self, root):
    #     if root.left is None and root.right is None:
    #         return [str(root.val)]

    #     result = []
    #     if root.left is None:
    #         result = result + ["#"]
    #     else:
    #         result = result + self.inOrder(root.left)

    #     if root is None:
    #         result = result + ["#"]
    #     else:
    #         result = result + [str(root.val)]

    #     if root.right is None:
    #         result = result + ["#"]
    #     else:
    #         result = result + self.inOrder(root.right)

    #     return result

s = Solution()
# print s.inOrder(lc.buildTree([5,4,1,None,1,None,4,2,None,2,None]))
# print s.inOrder(lc.buildTree([1, 2, 2, 3, 4, 4, 3]))
print s.isSymmetric(lc.buildTree([5,4,1,None,1,None,4,2,None,2,None]))
print s.isSymmetric(lc.buildTree([1, 2, 2, 3, 4, 4, 3]))
