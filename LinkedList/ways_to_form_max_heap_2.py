class Solution:
    # @param A : list of integers
    # @return an integer
    def ncr(self,n, r, p):
        num = 1
        den = 1
        for i in range(r):
            num = (num * (n - i)) % p
            den = (den * (i + 1)) % p
        return (num * pow(den, p - 2, p)) % p

    def findX(self,n):
        value = 1
        num = n
        while num > value:
            num -= value
            value *= 2
        X = min(value // 2, num) + (n - num) // 2
        return X

    def findAns(self,n):
        if n == 1 or n == 0:
            return 1
        m = 10 ** 9 + 7
        X = self.findX(n)
        return (self.ncr(n - 1, X, m)  * self.findAns(X) *self.findAns(n - 1 - X)) % m

    def findAns2(self, n):
        if n == 1 or n == 0 or n==2 :
            return 1
        m = 10 ** 9 + 7
        X = self.findX(n)
        c1 =   (self.ncr(n - 3, X - 2, m) * self.findAns2(X) * self.findAns(n - 1 - X)) % m
        c2 =  (self.ncr(n - 3,X , m) * self.findAns(X) * self.findAns2(n - 1 - X)) % m
        # print(c1,c2,c3)
        return c1+c2

    def find(self, n):
        if n == 1 or n == 0 or n == 2:
            return 1
        m = 10 ** 9 + 7
        X = self.findX(n)
        c1 = (self.ncr(n - 3, X - 1, m) * self.findAns(X) * self.findAns(n - 1 - X)) % m
        c2 = self.findAns2(n)
        return c1+c2
    def solve(self, A):
        n = len(A)
        maxx = max(A)
        c = A.count(maxx)
        if c == 1:
            return self.find(n)
        else:
            return self.findAns(n)

A = [ 15, 15, 35, 48, 49, 66 ]
ans = Solution().solve(A)
print(ans)