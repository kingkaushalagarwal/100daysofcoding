class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        dp = [0] * 60
        dp[1] = 1
        dp[2] = 1
        f1 = 1;
        f2 = 1
        for i in range(3, 60):
            f = f1 + f2
            dp[i] = f % 10
            f1 = f2
            f2 = f % 10
        i = A;
        count = 0
        while i % 60 != 0 and i <= B:
            if dp[i % 60] in [2, 3, 5, 7]:
                count += 1
            i += 1
        if i == B:
            return count
        fact = (B - i) // 60
        count += (fact) * 28
        i += fact * 60
        while i <= B:
            if dp[i % 60] in [2, 3, 5, 7]:
                count += 1
            i += 1
        return count


