#Serialize and deserialize
from collections import deque
from copy import deepcopy


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def preOrderT(self, root, arr):
        if root == None:
            return
        arr.append(str(root.val))
        self.preOrderT(root.left, arr)
        self.preOrderT(root.right, arr)

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        arr = []
        self.preOrderT(root, arr)
        return "$".join(arr)

    def find(self, l, r, arr, val):
        if l <= r:
            mid = (l + r) // 2
            if arr[mid] == val:
                return mid
            elif arr[mid] < val:
                return self.find(mid + 1, r, arr, val)
            else:
                return self.find(l, mid - 1, arr, val)
        return -1

    def createBst(self, preOrder, inOrder):
        if len(inOrder) == 0 or len(preOrder) == 0:
            return None
        value = preOrder[0]
        preOrder.popleft()
        node = TreeNode(value)
        index = self.find(0, len(inOrder) - 1, inOrder, value)
        node.left = self.createBst(preOrder, inOrder[:index])
        node.right = self.createBst(preOrder, inOrder[index + 1:])
        return node

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if data == '$' or data == '':
            return None
        preOrder = [int(x) for x in data.split("$")]
        inOrder = deepcopy(preOrder)
        inOrder.sort()
        preOrder = deque(preOrder)

        root = self.createBst(preOrder, inOrder)
        arr = []
        self.preOrderT(root, arr)
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans