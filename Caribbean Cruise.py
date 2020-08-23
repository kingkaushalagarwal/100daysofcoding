from collections import Counter
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        counter  = Counter(B)
        val = sorted(list(counter.values()),reverse = True)
        print(val,val[A-1])
        print(val[:20])
        return val[A-1]
A = 4
B = [ 1, 3, 1, 3, 10, 3, 6, 6, 13, 3 ]
ans =Solution().solve(A,B)
print(ans)

print("afdfa".upper())