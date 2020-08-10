#https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3414/
"""
Find all duplicates in array

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""


#Trie implemetation O(n*log(max_array_element))
class TrieNode:
    def __init__(self):
        self.z = None
        self.o = None
        self.end = 0

class Solution:
    def findDuplicates(self, nums):
        root = TrieNode()
        ans = []
        for i in range(len(nums)):
            temp = root
            X = nums[i]
            while X > 0:
                value = X & 1
                if value == 0:
                    if temp.z == None:
                        temp.z = TrieNode()
                    temp = temp.z
                elif value == 1:
                    if temp.o == None:
                        temp.o = TrieNode()
                    temp = temp.o
                X = X >> 1
                if X == 0:
                    temp.end += 1
                if X == 0 and temp.end > 0 and temp.end & 1 == 0:
                    ans.append(nums[i])

        return ans