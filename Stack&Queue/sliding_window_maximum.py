#InterviewBit
from collections import deque
class Solution:
    def slidingMaximum(self, A, B):
        if len(A)<=B:
            return [max(A)]
        dq = deque()
        ans = []
        for i in range(len(A)):
            if len(dq) == 0 or A[dq[-1]] >= A[i]:
                dq.append(i)
            else:
                while len(dq)!=0 and A[dq[-1]] < A[i]:
                    dq.pop()
                dq.append(i)

            if i>=(B-1):
                ans.append(A[dq[0]])
                if dq[0]==(i+1-B):
                    dq.popleft()
        return ans


A = [ 648, 614, 490, 138, 657, 544, 745, 582, 738, 229, 775, 665, 876, 448, 4, 81, 807, 578, 712, 951, 867, 328, 308, 440, 542, 178, 637, 446, 882, 760, 354, 523, 935, 277, 158, 698, 536, 165, 892, 327, 574, 516, 36, 705, 900, 482, 558, 937, 207, 368 ]
B = 9
ans = Solution().slidingMaximum(A,B)
print(ans)
# 10 9 8 7 6 5 4 3 2