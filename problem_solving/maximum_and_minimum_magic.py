class Solution:
    def solve(self, A):
        A.sort()
        minimum = 0
        maximum = 0
        print(A)
        for i in range(0, len(A), 2):
            minimum += abs(A[i] - A[i + 1])
        i = len(A) // 2 - 1;
        j = len(A) // 2
        while i > -1 and j < len(A):
            maximum += abs(A[i] - A[j])
            i -= 1
            j += 1
        return [maximum, minimum]

A =  [ -98, 54, -52, 15, 23, -97, 12, -64, 52, 85 ]
ans  = Solution().solve(A)
print(ans)