#interviewBit
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        B = [0]
        C = [len(A) + 1]
        n = len(A)
        for x in A:
            if x == (B[-1] + 1):
                B.append(x)
                while len(C) != 0 and C[-1] == B[-1] + 1:
                    B.append(C.pop())
            elif x < C[-1]:
                C.append(x)
            else:
                return 0
        return 1


