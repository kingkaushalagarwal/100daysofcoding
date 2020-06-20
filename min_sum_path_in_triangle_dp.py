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
        return findMin2(A)