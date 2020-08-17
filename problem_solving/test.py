from math import log


class TrieNode:
    def __init__(self):
        self.zero = None
        self.one = None


class Trie:
    def __init__(self):
        self.t = TrieNode()

    def add(self, num, length):
        temp = self.t
        c = 1 << (length - 1)
        print("add: ",num)
        for i in range(length):
            print(num&c)
            if num & c>0:
                if temp.one == None:
                    temp.one = TrieNode()
                temp = temp.one
            else:
                if temp.zero == None:
                    temp.zero = TrieNode()
                temp = temp.zero
            c = c >> 1
        print()
    def small(self, num, length):
        temp = self.t
        l = []
        ans = 0
        c = 1 << (length - 1)
        print("num: ",num)
        for i in range(length-1,-1,-1):
            print(num&c,end=" ")
            if num & c>0:
                if temp.one != None:
                    temp = temp.one
                    ans += 2 ** i
                else:
                    temp = temp.zero
            else:
                if temp.zero != None:
                    temp = temp.zero
                else:
                    temp = temp.one
                    ans += 2 ** i
            c = c >> 1
        print()
        return ans


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        maxx = max(max(A), max(B))
        length = int(log(maxx, 2)) + 1
        ans = []
        T = Trie()
        for x in A:
            T.add(x, length)
        for x in B:
            value = T.small(x, length)
            ans.append(value)
        return ans
A = [0, 1, 2, 3]
B = [1, 7]
ans = Solution().solve(A,B)
print(ans)