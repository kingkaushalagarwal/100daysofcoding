#Interview Bit
#window string
from collections import Counter
class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
	def minWindow(self, A, B):
        lockup = dict().fromkeys(B,0)
        contains = Counter(B)
        precheck = Counter(A)
        for key,val in contains.items():
            if (key not in A) or precheck[key]<contains[key]:
                return ""
                
        counting =Counter(B)
        i=0;j=0;start =0;end=len(A);minn = len(A)
        while i<len(A) and j<len(A):
            if len(contains)!=0:
                if A[i] in lockup:
                    lockup[A[i]]+=1
                if A[i] in contains:
                    contains[A[i]]-=1
                    if contains[A[i]]==0:
                        del contains[A[i]]
            while len(contains)==0 and j<len(A):
                length = i-j+1
                if length<minn:
                    minn = length
                    start =j;end=i
                if A[j] in lockup:
                    if lockup[A[j]]> counting[A[j]]:
                        lockup[A[j]]-=1
                    else:
                        lockup[A[j]]-=1
                        contains[A[j]] = 1
                j+=1
            i+=1    
        return A[start:end+1]    
                        
                        
                    
                    
                    
                