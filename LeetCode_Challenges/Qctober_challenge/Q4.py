#Removed covered intervals
from typing import List
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)

        c = 1
        s = intervals[0][0]
        e = intervals[0][1]
        for x in intervals:
            if x[1] <= e:
                continue
            elif s==x[0]:
                e = x[1]
            else:
                c += 1
                s = x[0]
                e = x[1]
        return c

intervals = [[1,2],[1,4],[3,4]]
ans =Solution().removeCoveredIntervals(intervals)
print(ans)