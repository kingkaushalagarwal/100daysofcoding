#interviewbit flip array 

class Solution:
    def calculate(self,A, num):
        maxx = 10 ** 9 + 7
        dp = [[0] * (num + 1) for i in range(len(A) + 1)]
        for i in range(1, num + 1):
            dp[0][i] = maxx
        for i in range(1, len(A) + 1):
            for j in range(1, num + 1):
                if j - A[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i - 1][j - A[i - 1]] + 1, dp[i - 1][j])
            # for i in range(len(A)+1):
            #     print(*dp[i])
        return dp[-1][-1]

    def findMin(self,A):
        dp = [[0] * (sum(A) + 1) for i in range(len(A) + 1)]
        for i in range(sum(A) + 1):
            dp[0][i] = i
        for i in range(1, len(A) + 1):
            num = A[i - 1] * 2
            for j in range(1, sum(A) + 1):
              if j < num:
                    dp[i][j] = dp[i - 1][j]
              else:
                    dp[i][j] = min(dp[i - 1][j - A[i - 1] * 2], dp[i - 1][j])
        # for i in range(len(A)+1):
        #     print(*dp[i])
        return dp[-1][-1]

    def solve(self, A):
        possible_min_element = self.findMin(A)
        print(possible_min_element)
        required_num = (sum(A) - possible_min_element)//2
        print(required_num)
        ans = self.calculate(A,required_num)
        return ans

A = [9,6]
ans = Solution().solve(A)
print(ans)