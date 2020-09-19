#Sequential digits
#https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3465/https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3465/

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        arr =[1,2,3,4,5,6,7,8,9]
        l =[]
        for i in range(9):
            num =0
            for j in range(i,9):
                num = num*10 + arr[j]
                l.append(num)
        ans = []
        for i in range(len(l)):
            if l[i]>=low and l[i]<high:
                ans.append(l[i])
        ans.sort()
        return ans