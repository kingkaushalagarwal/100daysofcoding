# Sum of Root To Leaf Binary Numbers
# https://leetcode.com/explore/featured/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3453/efinition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calculate(self, summ, l):
        binary = bin(summ)[2:]
        c = 0
        k = 1
        for ch in binary[::-1]:
            if ch == '1':
                c += (2 ** (l - k))
            k += 1
        return c

    def find(self, root, summ, l, total):
        if root.left == None and root.right == None:
            if root.val == 1:
                summ = summ + (2 ** l);
            l = l + 1
            val = self.calculate(summ, l)
            total[0] += val
            return

        c = 0
        if root.val == 1:
            c = 1
        if root.right == None:
            self.find(root.left, summ + (2 ** l) * c, l + 1, total)
        elif root.left == None:
            self.find(root.right, summ + (2 ** l) * c, l + 1, total)
        else:
            self.find(root.left, summ + (2 ** l) * c, l + 1, total)
            self.find(root.right, summ + (2 ** l) * c, l + 1, total)

    def sumRootToLeaf(self, root) -> int:
        total = [0]
        self.find(root, 0, 0, total)
        return total[0]