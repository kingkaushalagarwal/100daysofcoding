#All elements in two binary search tree
#https://leetcode.com/explore/featured/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3449/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,l):
        if root==None:
            return
        self.inorder(root.left,l)
        l.append(root.val)
        self.inorder(root.right,l)
    def getAllElements(self, root1, root2):
        l1=[]
        l2=[]
        self.inorder(root1,l1)
        self.inorder(root2,l2)
        ans =[]
        i=0;j=0
        while i<len(l1) and j<len(l2):
            if l1[i]<l2[j]:
                ans.append(l1[i])
                i+=1
            else:
                ans.append(l2[j])
                j+=1
        while i<len(l1):
            ans.append(l1[i])
            i+=1
        while j<len(l2):
            ans.append(l2[j])
            j+=1
        return ans