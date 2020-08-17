from collections import defaultdict
class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        d = defaultdict(int)
        ans = []
        for x in A:
            # print(x)
            if x[0]==1:
                n = x[1]
                v  = x[2]
                d[n]+=v
            else:
                n = x[1]
                c = 0
                while n>0:
                    if n in d:
                        c+=d[n]
                    n = n//2

                c+=d[0]
                ans.append(c)
        return ans
A = [[1, 1, 10], [1, 2, 5], [2, 3, 0], [2, 4, 0]]
ans = Solution().solve(A)
print(ans)