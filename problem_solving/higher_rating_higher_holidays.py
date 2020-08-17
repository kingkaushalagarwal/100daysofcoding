class Solution:
    def candy(self, A):
        if len(A) == 1:
            return 1
        ans = [0] * len(A)
        ans[0] = 1
        for i in range(len(A)):
            if A[i] > A[i - 1]:
                ans[i] = ans[i - 1] + 1
            else:
                ans[i] = 1
        for i in range(len(A) - 2, -1, -1):
            if A[i] > A[i + 1] and ans[i] <= ans[i + 1]:
                ans[i] = ans[i + 1] + 1
            else:
                ans[i] = max(ans[i], 1)

        if A[0] > A[1]:
            ans[0] = ans[1] + 1
        if A[-1] > A[-2]:
            ans[-1] = ans[-2] + 1
        return sum(ans)

