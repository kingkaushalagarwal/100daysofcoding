#Word Pattern
#https://leetcode.com/explore/featured/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3451/
class Solution:
    def check(self, l1, l2):
        n = len(l1)
        d = {}
        for i in range(n):
            if l1[i] not in d:
                d[l1[i]] = l2[i]
            else:
                if d[l1[i]] != l2[i]:
                    return False
        return True

    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        s = s.split()
        n1 = len(s)
        n2 = len(pattern)
        if n1 != n2:
            return False
        if self.check(pattern, s) and self.check(s, pattern):
            return True
        else:
            return False
pattern ="abba"
string ="cat dog dog cat"
ans =Solution().wordPattern(pattern,string)
print(ans)