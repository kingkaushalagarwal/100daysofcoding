#interview bit question
class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def solve(self, A, B):
		#memoization solution
        def calculate(i,B,d):
            if i==1 and B>0 and B<=9:
                return 1 
            elif i==1 and (B>9 or B==0):
                return 0
            if (i,B) in d:
                return d[(i,B)]
            ans = 0    
            for j in range(10):
                if B-j>=0:
                    ans += calculate(i-1,B-j,d)    
                else:
                    break
            d[(i,B)] = ans
            
            return ans  
        #tabulation solution 
		def calculate2(A,B):
            dp = [[0]*(B+1) for i in range(2)]
            m = (10**9)+7 
            for i in range(1,A+1):
                summ1 =0;summ2=0
                for j in range(1,B+1):
                    if i==1:
                        if j<=9:
                            dp[i%2][j] = 1
                        else:
                            break
                    else:
                        summ1 = (summ1%m + dp[(i-1)%2][j]%m)%m
                        if j>=10:
                            summ2 = (summ2%m +dp[(i-1)%2][j-10]%m)
                        dp[i%2][j]= summ1-summ2
            return dp[A%2][-1]%m              
        #d = {}
        #return calculate(A,B,d)%(10**9+7)
		return calculate2(A,B)%(10**9+7)