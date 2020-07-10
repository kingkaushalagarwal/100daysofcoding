import sys


class Solution:
    # @param A : string
    # @param B : string
    # @param C : string
    # @return an integer
    def isInterleave(self, A, B, C):
        d = {}

        def find(A, B, C, i, j, k):
            if k < 0:
                if (i >= 0 or j >= 0):
                    return 0
                else:
                    return 1
            # if (i, j, k) in d:
            #     return d[(i, j, k)]
            ans = None
            if i < 0:
                if B[j] == C[k]:
                    # ans = d[(i, j, k)] = ans
                    ans= find(A, B, C, i, j - 1, k - 1)
                else:
                    ans = 0
            elif j < 0:
                if A[i] == C[k]:
                    ans = find(A, B, C, i - 1, j, k - 1)
                else:
                    ans = 0
            elif A[i] != C[k] and B[j] != C[k]:
                ans = 0
            elif A[i] != C[k] and B[j] == C[k]:
                ans = find(A, B, C, i, j - 1, k - 1)
            elif A[i] == C[k] and B[j] != C[k]:
                ans = find(A, B, C, i - 1, j, k - 1)
            elif A[i] == C[k] and B[j] == C[k]:
                ans = find(A, B, C, i - 1, j, k - 1) or find(A, B, C, i, j - 1, k - 1)

            d[(i, j, k)] = ans
            return ans

        ans = find(A, B, C, len(A) - 1, len(B) - 1, len(C) - 1)
        return ans
A = "LgR8D8k7t8KIprKDTQ7aoo7ed6mhKQwWlFxXpyjPkh"
B = "Q7wQk8rqjaH971SqSQJAMgqYyETo4KmlF4ybf"
C = "Q7wLgR8D8Qkk7t88KIrpqjarHKD971SqSQJTQ7aoAMgoq7eYd6yETmhoK4KmlQwWFlF4xybXfpyjPkh"
# if (len(A)+len(B))!=len(C):
#     print(0)
#     sys.exit(0)
ans = Solution().isInterleave(A,B,C)
print(ans)