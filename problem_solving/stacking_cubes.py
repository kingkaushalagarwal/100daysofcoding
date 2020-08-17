import math
class Solution:
    # @param A : integer
    # @return an integer
    def findFactor(self,n):
        count =0
        for i in range(1,int(math.sqrt(n))+1):
            if n%i==0:
                count+=1
                if i!=(n//i):
                    count+=1
        return count -1
    def solve(self, A):
        return self.findFactor(A)
A= 4
ans = Solution().solve(A)
print(ans)