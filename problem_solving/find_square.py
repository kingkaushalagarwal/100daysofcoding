from math import sqrt


class Solution:
    # @param A : integer
    # @return an integer
    def find(self, i, summ, A, c, maxx):
        if i >= len(A):
            return
        if c == 0 and A[i] == '0':
            return self.find(i + 1, summ, A, c, maxx)
        value = summ * 10 + int(A[i])
        if self.check(value):
            maxx[0] = max(maxx[0], c + 1)
        self.find(i + 1, summ, A, c, maxx)
        self.find(i + 1, value, A, c + 1, maxx)

    def check(self, num):
        val = sqrt(num)
        val -= round(val)
        return True if val == 0 else False

    def solve(self, A):
        if self.check(A):
            return 0
        A = list(str(A))
        maxx = [-1]
        c = self.find(0, 0, A, 0, maxx)
        if maxx[0] == -1:
            return maxx[0]
        else:
            return len(A) - maxx[0]