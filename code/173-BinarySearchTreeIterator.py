# Link: https://leetcode.com/problems/binary-search-tree-iterator/
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import lc

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        if root is None:
            self._cur = None
        else:
            self._root = root
            self._cur = root
            self._prev = []
            while self._cur.left is not None:
                self.pushPrev(self._cur)
                self._cur = self._cur.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._cur is not None

    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext():
            return None

        rtn = self._cur.val

        trav = self._cur
        if trav.right is not None:
            trav = trav.right
            self.pushPrev(trav)

            while trav.left is not None:
                trav = trav.left
                self.pushPrev(trav)

        self._cur = self.popPrev()

        return rtn

    def popPrev(self):
        if len(self._prev) == 0:
            return None

        last = self._prev[-1]
        self._prev = self._prev[:-1]
        return last

    def pushPrev(self, node):
        self._prev.append(node)

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())


# tr1 = BSTIterator(lc.buildTree([1, 2, 2, 3, 4, 4, 3]))
tr1 = BSTIterator(lc.buildTree([5,4,1,None,1,None,4,2,None,2,None]))

print tr1.next()
print tr1.next()
print tr1.next()
print tr1.next()
print tr1.next()
print tr1.next()
print tr1.next()
print tr1.next()
print tr1.next()
print tr1.next()
print tr1.next()
