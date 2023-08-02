# 1. Binary Tree:
class tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
root = tree(1)
root.left = tree(2)
root.right = tree(3)
root.left.left = tree(4)

#2. Height of tree:
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def height(node):
    if node is None:
        return 0
    else:
        l_height = height(node.left)
        r_height = height(node.right)
        if (l_height > r_height):
            return l_height+1
        else:
            return r_height+1
root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
print("Height of tree is:", (height(root)))

#3. In-order, Pre-order, Post-order and DFS also:
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end = ' ')
        inorder(root.right)
def preorder(root):
    if root:
        print(root.data, end = ' ')
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=' ')
root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
print("Inorder of tree:" )
inorder(root)
print("\nPreorder of tree:" )
preorder(root)
print("\nPostorder of tree:" )
postorder(root)

#4. Find all leaves:
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def leaves(root):
    if not root:
        return
    if (not root.left and not root.right):
        print(root.data, end=' ')
    if root.left:
        leaves(root.left)
    if root.right:
        leaves(root.right)
root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
print(leaves(root))

#5. BFS:
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def bfs(root):
    if not root:
        return 
    t = []
    t.append(root)
    while len(t)>0:
        currnode = t.pop(0)
        print(currnode.data, end=' ')
        if currnode.left is not None:
            t.append(currnode.left)
        if currnode.right is not None:
            t.append(currnode.right)
root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
bfs(root)

#6. Sum of left leaves:
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def isLeaf(node):
    if node is None:
        return False
    if node.left is None and node.right is None:
        return True
    return False
def sum(root):
    res = 0
    if root is not None:
        if isLeaf(root.left):
            res += root.left.data
        else:
            res += sum(root.left)
        res += sum(root.right)
    return res

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
print("\nSum of left leaves:", sum(root))

#7. Sum of all nodes:
def SumNodes(l):
    leafNodeCount = pow(2, l - 1)
    vec = [[] for i in range(l)]
    for i in range(1, leafNodeCount + 1):
        vec[l - 1].append(i)
    for i in range(l - 2, -1, -1):
        k = 0
        while (k < len(vec[i + 1]) - 1):
            vec[i].append(vec[i + 1][k] +
                          vec[i + 1][k + 1])
            k += 2
    Sum = 0
    for i in range(l):
        for j in range(len(vec[i])):
            Sum += vec[i][j]
    return Sum
l = 3
print("\n Sum of all nodes:", SumNodes(l))

#8. count subtree:
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def Subtrees(root, count, x):
    if (not root):
        return 0
    ls = Subtrees(root.left,count,x)
    rs = Subtrees(root.right,count,x)
    Sum = ls + rs + root.data
    if (Sum == x):
        count[0] += 1
    return Sum
def count(root,x):
    if (not root):
        return 0
    count = [0]
    ls = Subtrees(root.left,count,x)
    rs = Subtrees(root.right,count,x)
    if ((ls + rs + root.data) == x):
        count[0] += 1
    return count[0]
root = Tree(5)
root.left = Tree(-10)
root.right = Tree(3)
root.left.left = Tree(9)
root.left.right = Tree(8)
root.right.left = Tree(-4)
root.right.right = Tree(7)
x = 7
print("Count =", count(root,x))

#9. Maximum level sum:
from collections import deque
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def Maximum(root):
    if (root == None):
        return 0
    result = root.data
    q = deque()
    q.append(root)
    while (len(q) > 0):
        count = len(q)
        sum = 0
        while (count > 0):
            temp = q.popleft()
            sum = sum + temp.data
            if (temp.left != None):
                q.append(temp.left)
            if (temp.right != None):
                q.append(temp.right)
            count -= 1
        result = max(sum, result)
    return result
root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
root.right.right = Tree(8)
root.right.right.left = Tree(7)
print("Maximum level sum is", Maximum(root))

#10. Find all odd level nodes:
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def oddnodes(root, isodd=True):
    if not root:
        return
    if isodd:
        print(root.data, end=' ')
    oddnodes(root.left, not isodd)
    oddnodes(root.right, not isodd)
root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
oddnodes(root)





