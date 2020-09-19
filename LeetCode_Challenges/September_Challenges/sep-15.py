#length of last word
#https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3461/
class Solution(object):
    def lengthOfLastWord(self, s):
        l = s.split()
        if len(l) == 0:
            return 0
        else:
            return len(l[-1])
