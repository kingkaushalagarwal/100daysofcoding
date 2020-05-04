#interview Bit 
#Lightsbers
from collections import Counter
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def check(self,A,B):
        counter = Counter(A)
        for i in range(len(B)):
            n=B[i]
            if (i+1 not in counter) or counter[i+1]<n:
                return False
        return True        
            
    def solve(self, A, B):
        if len(A)<sum(B) or self.check(A,B)==False:
            return -1
        minn = len(A)-sum(B)
        i=0;j=0;count =0
        C =[0]*len(B);length =0
        while i<len(A) and j<len(A):
            if count!=sum(B):
                num = A[i]; ind = num-1
                if ind>=0 and ind<len(B):
                    if C[ind]>=B[ind]:
                        count+=0
                    else:
                        # print(ind)
                        count+=1
                    C[ind]+=1
            while count==sum(B) and j<len(A):
                length = i-j+1 - sum(B)
                minn = min(minn,length)
                num = A[j]
                ind = num -1
                if ind>=0 and ind<len(B):
                    if C[ind]<=B[ind] and C[ind]>0:
                        count-=1
                    C[ind]-=1    
                j+=1
            i+=1
        return minn    