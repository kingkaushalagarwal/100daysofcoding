from testInput import input
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def summ(self, A, B, C, n, m):
        if n == 0:
            return 1
        if n == 1:
            return 1
        # odd
        if n & 1 == 1:
            return (((n - 1) * C) % m + (B * ((n * (n + 1)) // 2 - 1)) % m + (
                        self.summ(A, B, C, n // 2, m) * 2 * A) % m) % m +1
        elif n!=2 :
            return (((n - 1) * C) % m + (B * ((n * (n + 1)) // 2 - 1)) % m + (
                        (self.summ(A, B, C, n // 2, m) + self.summ(A, B, C, n // 2 - 1, m)) % m) * A % m) % m +1
        else:
            return ((n - 1) * C) % m + (B * ((n * (n + 1)) // 2 - 1)) % m + ( (self.summ(A, B, C, n // 2, m)% m) * A % m) +1

    def summ1(self, A, B, C, n, m):
        if n == 0 or n == 1:
            return 1
        print("Hello")
        # odd
        if n & 1 == 1:
            return (((n - 1) * C) % m + (B * ((n * (n + 1)) // 2 - 1)) % m + (
                        self.summ(A, B, C, n // 2, m) * 2 * A) % m) % m + 1
        elif n != 2:
            return (((n - 1) * C) % m + (B * ((n * (n + 1)) // 2 - 1)) % m + (
                        (self.summ(A, B, C, n // 2, m) + self.summ(A, B, C, n // 2 - 1, m)) % m) * A % m) % m + 1
        else:
            return (((n - 1) * C) % m + (B * ((n * (n + 1)) // 2 - 1)) % m + (
                        (self.summ(A, B, C, n // 2, m)) % m) * A % m) % m + 1

    def solve(self, A, B, C, D):
        if D == 1:
            return 1
        m = (10 ** 9 + 7)
        return self.summ1(A, B, C, D, m) % m
A,B,C = map(int,input().split())
for i in range(1,7):
    D =i
    ans = Solution().solve(A,B,C,D)
    print(ans)
