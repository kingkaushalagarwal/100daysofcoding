#K-difference pairs in array
from typing import List
from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        res = 0
        for i in c:
            if k>0 and i+k in c or k==0 and c[i]>1:
                res+=1
        return res