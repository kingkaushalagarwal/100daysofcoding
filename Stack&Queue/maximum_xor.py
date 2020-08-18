from math import log

class TrieNode:
    def __init__(self):
        self.zero = None
        self.one = None
class Trie:
    def __init__(self, length):
        self.t = TrieNode()
        self.size = length

    def add(self, num):
        temp = self.t
        p = 1 << (self.size - 1)
        for i in range(self.size):
            if p & num:
                if temp.one == None:
                    temp.one = TrieNode()
                temp = temp.one
            else:
                if temp.zero == None:
                    temp.zero = TrieNode()
                temp = temp.zero
            p = p >> 1

    def findXor(self, num):
        temp = self.t
        p = 1 << (self.size - 1)
        count = 0
        for i in range(self.size):
            if p & num:
                if temp.zero != None:
                    temp = temp.zero
                    count += p
                else:
                    temp = temp.one
            else:
                if temp.one != None:
                    temp = temp.one
                    count += p
                else:
                    temp = temp.zero
            p = p >> 1
        return count


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        maxx = max(A)
        if maxx == 0:
            return 0
        length = int(log(maxx, 2)) + 1
        T = Trie(length)
        maxx = float('-inf')
        for i in range(len(A)):
            if i != 0:
                val = T.findXor(A[i])
                maxx = max(maxx, val)
            T.add(A[i])
        return maxx

