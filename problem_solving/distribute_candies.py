#InterviewBit
#using observation
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if A==2:
            return min(B,C)
        c=2
        x = (B+C)//A
        while c<A:
            if B>C:
                B-=x
            else:
                C-=x
            c+=1
        return min(x,B,C)

#using binary search
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def check(self,A,B,C,x):
        temp = B//x + C//x
        if temp>=A:
            return True
        return False
    def solve(self, A, B, C):
        l=1
        h = B+C
        ans=-1
        while l<=h:
            mid = (l+h)//2
            if self.check(A,B,C,mid):
                ans = mid
                l= mid+1
            else:
                h = mid-1
        return ans