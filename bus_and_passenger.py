#InterviewBit
#Bus and passenger 
class Solution:
    # @param A : list of integers
    # @param B : string
    # @return a list of integers
    def solve(self, A, B):
        arr =[]
        for i in range(len(A)):
            arr.append([A[i],i+1])
        arr.sort()
        stack=[]
        i=0;ans=[]
        for v in B:
            if v=='0':
                stack.append(arr[i][1])
                ans.append(arr[i][1])
                i+=1
            else:
                val = stack.pop()
                ans.append(val)
        return ans        