#InterviewBit
#Divide Integers
class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def UsingSubstraction(self,A,B):
	   count =0
	   sign = False
	   maxx = 2**31-1
	   if (B==1 and A>0) or (B==-1 and A<0):
	       ans = min(maxx,abs(A))
	       return ans
	   elif (B==1 and A<0) or (B==-1 and A>0):
	       ans = min(maxx+1,abs(A))
	       return -ans
	   if A>0 and B>0 or A<0 and B<0:
	       sign = True
	   A = abs(A);B= abs(B)
	   while A>=B:
	        A-=B
	        count+=1
	   if sign:
	       return count
	   return - count    

	def UsingBits(self,A,B):
	    sign = 1
	    maxx = 2**31-1
	    if (A>0 and B>0) or (A<0 and B<0):
	        sign = 1
        else:
            sign = -1 
        A = abs(A)
        B= abs(B)
        temp = 0
        quotient = 0
        for i in range(31,-1,-1):
            if (temp + (B<<i))<=A:
	            temp +=  B<<i
	            quotient = quotient | 1<<i
	    if sign==1:
	        quotient = min(maxx,quotient)
	    else:
	        quotient = min(maxx+1,quotient)
	        
	    return sign*quotient        
	    
	def divide(self, A, B):
	   return self.UsingBits(A,B)
	   
	   
	   