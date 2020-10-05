from typing import List
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if len(matrix) == 0:
            self.matrix = None
        else:
            self.n = len(matrix)
            self.m = len(matrix[0])
            for i in range(self.n):
                prev = 0
                for j in range(self.m):
                    matrix[i][j] += prev
                    prev = matrix[i][j]
            for i in range(self.m):
                prev = 0
                for j in range(self.n):
                    matrix[j][i] += prev
                    prev = matrix[j][i]
            self.matrix = matrix

    def check(self, r, c):
        return r >= 0 and r < self.n and c >= 0 and c < self.m

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a = 0;
        b = 0;
        c = 0
        if self.check(row1 - 1, col2):
            a = self.matrix[row1 - 1][col2]
        if self.check(row2, col1 - 1):
            b = self.matrix[row2][col1 - 1]
        if self.check(row1 - 1, col1 - 1):
            c = self.matrix[row1 - 1][col1 - 1]
        return self.matrix[row2][col2] - a - b + c

matrix =[
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
obj = NumMatrix(matrix)
print(obj.sumRegion(2,1,4,3))
print(obj.sumRegion(1,1,2,2))
print(obj.sumRegion(1,2,2,4))


# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12