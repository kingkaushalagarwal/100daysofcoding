#interviewBit
#using euler totient function good question
"""
Euler’s totient function denoted as phi(N), is an arithmetic function that counts the positive integers less than or equal to N that are relatively prime to N.
The idea is to use the following properties of Euler Totient function i.e.
F(n) = n*[multiple of (1- 1/p)] where p is prime factors of n

The formula basically says that the value of Φ(n) is equal to n multiplied by product of (1 – 1/p) for all prime factors p of n. For example value of Φ(6) = 6 * (1-1/2) * (1 – 1/3) = 2.
For a prime number p, Φ(p) is p-1. For example Φ(5) is 4, Φ(7) is 6 and Φ(13) is 12. This is obvious, gcd of all numbers from 1 to p-1 will be 1 because p is a prime.
"""
import math
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def seive(self, B):
        dp = [True] * (B + 1)
        dp[0] = False
        dp[1] = False
        for i in range(2, int(math.sqrt(B)) + 1):
            if dp[i] == True:
                for j in range(i * i, B + 1, i):
                    dp[j] = False
        return dp

    def expo(self, n, p, B):
        if p == 0:
            return 1
        elif p == 1:
            return n % B
        elif p & 1:
            return (n * self.expo((n % B * n % B), p // 2, B)) % B
        else:
            return self.expo((n * n) % B, p // 2, B)

    def gcd(self, a, b):
        if a == 0:
            return b
        return self.gcd(b % a, a)

    def totientFunction(self, m, prime):
        if m == prime:
            return m - 1
        count = 1
        for i in range(2, m):
            if self.gcd(i, m) == 1:
                count += 1
        return count


    #optimise function to compute euler totient of n numbers
    def computeTotient(self, N):
        phi = [0] * (N)
        for i in range(1, N):
            phi[i] = i
        # Compute other Phi values
        for p in range(2, N):
            # If phi[p] is not computed already,
            # then number p is prime
            if (phi[p] == p):
                # Phi of a prime number p
                # is always equal to p-1.
                phi[p] = p - 1
                # Update phi values of all
                # multiples of p
                for i in range(2 * p, N, p):
                    # Add contribution of p to its
                    # multiple i by multiplying with
                    # (1 - 1/p)
                    phi[i] = (phi[i] // p) * (p - 1)
        return phi

    def mysterious_function(self, A, B):
        if B == 1:
            return 0
        phi = self.computeTotient(B + 1)
        n = len(A)
        module = [0] * n
        module[-1] = B
        value = B
        start = -1
        for i in range(n - 2, -1, -1):
            value = phi[value]
            module[i] = value
            if value == 1:
                start = i
                break
        if start == -1:
            start = 0
        ans = 1
        for i in range(start, n):
            ans = self.expo(A[i], ans, module[i])
        return ans
