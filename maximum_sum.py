#InterviewBit
'''
#Maximum Sum
Problem Description
You are given an array A of N integers and three integers B, C, and D. You have to find the maximum value of A[i]*B + A[j]*C + A[k]*D, where 1 <= i <= j <= k <= N.    

Problem Constraints
1 <= N <= 105 -10000 <= A[i], B, C, D <= 10000    
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        arr3 = [x*D for x in A]
        n = len(A)
        for i in range(n-2,-1,-1):
            arr3[i]=max(arr3[i],arr3[i+1])
        
        for i in range(n):
            arr3[i] += A[i]*C
            
        for i in range(n-2,-1,-1):
            arr3[i]=max(arr3[i],arr3[i+1]) 
        
        for i in range(n):
            arr3[i] += A[i]*B    
        
        return max(arr3)