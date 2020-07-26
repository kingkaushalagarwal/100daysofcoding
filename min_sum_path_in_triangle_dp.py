from copy import deepcopy
#InterviewBit Min Sum Path in Triangle
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        def findMin2(arr):
            if len(arr)==1:
                return arr[0][0]
            for i in range(len(arr)-1):
                for j in range(len(arr[i])):
                    if j==0:
                        arr[i+1][j]= arr[i][j]+arr[i+1][j]
                    else:
                        arr[i+1][j] = min(arr[i+1][j] + arr[i][j] , arr[i+1][j]+arr[i][j-1])
                arr[i+1][-1] = arr[i][-1]+ arr[i+1][-1]
        #    for i in range(len(arr)):
        #        print(*arr[i])
            return min(arr[-1])
        # return findMin2(A)
	#Bottom up approach using 1-D array from interviewBit hint section	
	    def Alternate(arr):
            n = len(arr[-1])
            dp=deepcopy(arr[-1])
            for i in range(n-2,-1,-1):
                for j in range(0,i+1):
                    dp[j]= min(dp[j],dp[j+1]) + arr[i][j]
            return dp[0]        
        return Alternate(A)