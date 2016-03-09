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
        left = TreeNode(arr[i+1])
        node.left = left
        queue.append(left)

        if i+2 >= len(arr):
            break
        right = TreeNode(arr[i+2])
        node.right = right
        queue.append(right)

        i += 2

    return root
