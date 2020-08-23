from collections import deque


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def check(self, r, c):
        return r >= 0 and r < 8 and c >= 0 and c < 8

    def solve(self, A, B, C, D):
        if A == C and B == D:
            return 0
        row = [1, 1, -1, -1]
        col = [1, -1, 1, -1]
        queue = deque()
        queue.append([A - 1, B - 1, 0])
        ans = -1
        visited = [[False] * 8 for i in range(8)]
        visited[A - 1][B - 1] = True

        while len(queue) != 0:
            ind1, ind2, d = queue.popleft()

            for i in range(4):
                r = ind1
                c = ind2

                while self.check(r + row[i], c + col[i]):
                    r += row[i]
                    c += col[i]
                    if r == (C - 1) and c == (D - 1):
                        return d + 1

                    if visited[r][c] == False:
                        visited[r][c] = True
                        queue.append([r, c, d + 1])

        return -1




