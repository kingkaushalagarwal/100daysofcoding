from collections import deque
class Solution:
    # @param A : string
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        queue =deque()
        count =0
        maxx =  -99999
        for i in range(len(A)):
            ind = ord(A[i]) - 97
            if B[ind]==1:
                if (count+1)>C:
                    maxx = max(maxx,len(queue))
                    while queue and (count+1)>C:
                        ind = ord(queue.popleft())-97
                        if B[ind]==1:
                            count-=1
                count+=1
            queue.append(A[i])
        maxx = max(maxx,len(queue))
        return maxx