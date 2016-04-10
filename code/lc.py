# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(arr):
    root = TreeNode(arr[0])
    queue = [root]
    i = 0
    while True:
        node = queue[0]
        queue = queue[1:]

        if i+1 >= len(arr):
            break
        if arr[i+1] is not None:
            left = TreeNode(arr[i+1])
            node.left = left
            queue.append(left)

        if i+2 >= len(arr):
            break
        if arr[i+2] is not None:
            right = TreeNode(arr[i+2])
            node.right = right
            queue.append(right)

        i += 2

    return root

def getTrees():
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.left.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    root.left.left.right = TreeNode(5)
    root.left.left.left = TreeNode(6)
    root.left.left.left.left = TreeNode(7)

    return [root, root.left.left, root.right, root.left.right,
            TreeNode(0),
            buildTree(range(3)), buildTree(range(4)), buildTree(range(113))]

def treeHeight(root):
    if root is None:
        return 0

    leftDepth = treeHeight(root.left)
    rightDepth = treeHeight(root.right)

    return max(leftDepth, rightDepth) + 1
