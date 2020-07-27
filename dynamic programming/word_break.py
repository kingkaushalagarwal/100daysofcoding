#important question
#observation important for reducing time complexity
class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):
        n = len(A)
        dp = [0] * n
        flag = False
        maxx = max(len(s) for s in B)
        B = dict().fromkeys(B, 1)

        for i in range(n):
            substring1 = A[0:i + 1]

            if len(substring1) <= maxx and substring1 in B:
                dp[i] = 1;
                if i + 1 == n:
                    flag = True
            if dp[i] != 0:
                for j in range(i + 1, n):
                    length = j - i
                    if length > (maxx + 1):
                        break
                    substring2 = A[i + 1:j + 1]
                    if substring2 in B:
                        dp[j] = 1
                        if j + 1 == n:
                            flag = True
            if flag:
                break
        return dp[-1]