from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        n = len(intervals)
        if n == 0:
            return [newInterval]

        s = newInterval[0]
        e = newInterval[1]
        minn = s
        maxx = e
        for i in range(n):
            x = intervals[i]
            start = x[0]
            end = x[1]
            if start <= s and end >= s:
                minn = min(minn, start)
                intervals[i] = [-1, -1]
            if start <= e and end >= e:
                maxx = max(maxx, end)
                intervals[i] = [-1, -1]
            if s <= start and e >= start:
                intervals[i] = [-1, -1]
            if s <= end and e >= end:
                intervals[i] = [-1, -1]

        flag = False
        ans = []

        # newInterval is smallest
        if maxx < intervals[0][0]:
            ans.append([minn, maxx])
            flag = True

        for i in range(n):
            # having some overlapping interval
            if intervals[i] == [-1, -1]:
                if flag == False:
                    flag = True
                    ans.append([minn, maxx])
            else:
                ans.append(intervals[i])

            # having no overlapping interval
            if (i + 1) < n and flag == False:
                if intervals[i][1] < minn and intervals[i + 1][0] > maxx:
                    ans.append([minn, maxx])

        # newInterval is largest
        if minn > intervals[-1][1] and flag == False:
            ans.append([minn, maxx])
        return ans

intervals=[[1,5]]
newInterval=[2,3]
ans = Solution().insert(intervals,newInterval)
print(ans)