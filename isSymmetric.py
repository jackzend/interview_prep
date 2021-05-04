# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(arr,n):
    count = 0
    q = []
    root = TreeNode(arr[0])
    q.append(root)
    curr = None

    for i in range(1,n):
        node = TreeNode(arr[i])
        if count == 0:
            curr = q.pop(0)
        if count == 0:
            count += 1
            curr.left = node
        else:
            count = 0
            curr.right = node
        if arr[i] != -101:
            q.append(node)
    return root

test1 = [1,2,2,3,4,4,3]
test2 = [2,3,3,4,5,5,4,-101,-101,8,9,-101,-101,9,8]

tree1 = buildTree(test1,len(test1))
tree2 = buildTree(test2,len(test2))

x = 1

def isSymmetric(root):
        """
        :type root: TreeNode
        :rtype: bool
        """

print(isSymmetric(tree1))
print(isSymmetric(tree2))