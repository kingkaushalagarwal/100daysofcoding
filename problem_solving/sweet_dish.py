#InterviewBit
#recursion question
from math import sqrt
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def prime(self, x):
        if x < 2:
            return False
        if x == 2 or x == 3:
            return True
        for i in range(2, int(sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    def find(self, A, B, C, isPrime, flag, i, summ):
        if i < 0:
            if flag and summ >= B and summ <= C:
                return 1
            else:
                return 0
        else:
            # not taken
            a = self.find(A, B, C, isPrime, flag, i - 1, summ)
            if isPrime[i] == True:
                b = self.find(A, B, C, isPrime, True, i - 1, summ + A[i])
            else:
                b = self.find(A, B, C, isPrime, flag, i - 1, summ + A[i])
            return a + b

    def solve(self, A, B, C):
        isPrime = [False] * len(A)
        for i in range(len(A)):
            if self.prime(A[i]):
                isPrime[i] = True
        return self.find(A, B, C, isPrime, False, len(A) - 1, 0)


A = [ 43, 13, 51, 97, 29 ]
B = 9
C = 136
ans  = Solution().solve(A,B,C)
print(ans)