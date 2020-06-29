#InterviewBit
#GCD Ordering
#corner cases - no more than one element whose frequency is two.
#if array contains two zero than only input array acceptable if it has all zeros.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def gcd(self,a,b):
        if a==0:
            return b
        return   self.gcd(b%a,a)
        
    def solve(self, A):
        if len(A)<3:
            if len(A)==2:
                if A[0]<A[1]:
                    A[0],A[1]=A[1],A[0]
            return A    
            # return 
        A.sort()
        x=A[0];y=A[1];flag = True
        for i in range(2,len(A)-1):
            g = self.gcd(x,y)
            num = g + y
            if A[i]==num:
                x =y
                y = A[i]
                continue
            else:
                flag = False
        if flag==False:
            return [-1]
        g = self.gcd(A[-2],A[-3])
        if g+A[-2]==A[-1]:
            return A
        g = self.gcd(A[-1],A[0])
        if g+A[0]==A[1]:
            temp = A[-1]
            for i in range(len(A)-1,0,-1):
                A[i]=A[i-1]
            A[0]=temp
            return A
        return   [-1]  