#InterviewBit
'''
#Maximum Sum
Problem Description
You are given an array A of N integers and three integers B, C, and D. You have to find the maximum value of A[i]*B + A[j]*C + A[k]*D, where 1 <= i <= j <= k <= N.    

Problem Constraints
1 <= N <= 105 -10000 <= A[i], B, C, D <= 10000    
'''
#Approach 1
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


#Approach 2
def solve(A,B,C,D):
    n = len(A)
    dp = [[-5e9 for i in range(3)] for j in range(n+1)]
    for i in range(1,n+1):
        dp[i][0]=max(dp[i-1][0],A[i-1]*B)
        dp[i][1]=max(dp[i-1][1],dp[i][0] + A[i-1]*C)
        dp[i][2] = max(dp[i-1][2],dp[i][1] + A[i-1]*D)
    return dp[n][2]
    
   
A = [1, 5, -3, 4, -2]
B = 2
C = 1
D = -1    
ans  =solve(A,B,C,D)
print(ans)
 		