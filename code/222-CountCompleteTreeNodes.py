from lc import *

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        depth = self.leftMostDepth(root)

        path = self.pathToEnd(root, [], depth)
        nLeaves = self.leavesCount(path, 0)
        nComplete = 2 ** len(path) - 1

        return nLeaves + nComplete

    def leavesCount(self, path, count):
        if len(path) == 1:
            return count + path[0] + 1

        return self.leavesCount(
            path[1:], count + path[0] * (2 ** len(path[1:])))

    def pathToEnd(self, root, path, depth):
        if depth == 0:
            return path
        if root.left is None and root.right is None:
            return path

        if self.rightMostDepth(root.left) == depth-1:
            if root.right is None or self.leftMostDepth(root.right) < depth-1:
                return path + [0] + [1] * (depth-1)
            else:
                return self.pathToEnd(root.right, path + [1], depth-1)
        else:
            return self.pathToEnd(root.left, path + [0], depth-1)

    def leftMostDepth(self, root):
        depth = 0
        node = root.left
        while node is not None:
            depth += 1
            node = node.left
        return depth

    def rightMostDepth(self, root):
        depth = 0
        node = root.right
        while node is not None:
            depth += 1
            node = node.right
        return depth


s = Solution()
# root = buildTree([0, 1, 3, 5, 65, 2, 34, 56, 2, 1, 3])
root = buildTree([0, 1, 2, 3])
s.pathToEnd(root)
