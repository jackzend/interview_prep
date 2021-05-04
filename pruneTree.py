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
        if arr[i] != None:
            node = TreeNode(arr[i])
        else:
            node = None
        if count == 0:
            curr = q.pop(0)
        if count == 0:
            count += 1
            curr.left = node
        else:
            count = 0
            curr.right = node
        if arr[i] != None:
            q.append(node)
    return root

test1 = [1,None,0,0,1]
tree1 = buildTree(test1,len(test1))
test2 = [1,1,0,1,1,0,1,0]
tree2 = buildTree(test2,len(test2))

test3 = [1,0,1,0,0,0,1]

tree3 = buildTree(test3,len(test3))


def isLeaf(node):
    return not node.left and not node.right


def pruneChild(parent, child):
    if child == parent.right:
        parent.right = None
        return parent
    parent.left = None
    return parent


def pruneTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root == None:
        return None

    if not root.left and not root.right:  # leaf root
        if root.val == 1:
            return root
        return None
    root = pruneTreeHelper(root)
    return final_prune(root)

def final_prune(root):
    for child in [root.left, root.right]:
        if child:
            if isLeaf(child):
                if child.val == 0:
                    root = pruneChild(root,child)
    return root
def pruneTreeHelper(root):  # root has at least one child

    for child in [root.left, root.right]:
        if child != None:  # don't do anything if left or right is none
            if isLeaf(child):  # our child is a leaf
                if child.val == 0:
                    # prune
                    root = pruneChild(root, child)
                # else do nothing must have 1 valued leafs
            else:  # this child is not a leaf
                if child == root.left:
                    root.left = pruneTreeHelper(child)
                else:
                    root.right = pruneTreeHelper(child)

    return root

out1 = pruneTree(tree1)
out2 = pruneTree(tree2)
out3 = pruneTree(tree3)

x = 1