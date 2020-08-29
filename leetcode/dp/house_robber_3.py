# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find(self, root):
        if root == None:
            return [0, 0]
        left = self.find(root.left)
        right = self.find(root.right)
        prev_parent = left[0] + right[0]
        prev = max(left[1] + right[1] + root.val, prev_parent, left[0] + right[1], right[0] + left[1])
        return [prev, prev_parent]

    def rob(self, root):
        if root == None:
            return 0

        value = self.find(root)
        return max(value[0], value[1])