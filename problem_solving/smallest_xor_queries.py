class TrieNode:
    def __init__(self):
        self.zero = None
        self.one = None


class Trie:
    def __init__(self):
        self.t = TrieNode()

    def add(self, string):
        temp = self.t
        for x in string:
            if x == '1':
                if temp.one == None:
                    temp.one = TrieNode()
                temp = temp.one
            else:
                if temp.zero == None:
                    temp.zero = TrieNode()
                temp = temp.zero

    def small(self, string):
        temp = self.t
        l = []
        for x in string:
            if x == '1':
                if temp.one != None:
                    temp = temp.one
                    l.append('1')
                else:
                    temp = temp.zero
                    l.append('0')
            else:
                if temp.zero != None:
                    temp = temp.zero
                    l.append('0')
                else:
                    temp = temp.one
                    l.append('1')
        return ''.join(l)


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        def convert(binary):
            n = len(binary)
            c = 0
            ans = 0
            for x in binary[::-1]:
                if x == '1':
                    ans += (2 ** c)
                c += 1
            return ans

        maxx = max(max(A), max(B))
        length = len(bin(maxx)[2:])
        ans = []
        T = Trie()
        for x in A:
            string = '{:0>{}}'.format(bin(x)[2:], length)
            T.add(string)
        for x in B:
            string = '{:0>{}}'.format(bin(x)[2:], length)
            value = T.small(string)
            ans.append(convert(value))
        return ans
