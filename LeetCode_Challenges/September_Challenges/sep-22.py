class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return nums
        var1 = None;
        var2 = None
        count1 = 0;
        count2 = 0
        for x in nums:
            if var1 == x:
                count1 += 1
            elif var2 == x:
                count2 += 1
            elif count1 == 0:
                var1 = x
                count1 = 1
            elif count2 == 0:
                var2 = x
                count2 = 1

            else:
                count1 = max(count1 - 1, 0)
                count2 = max(count2 - 1, 0)
        c1 = 0;
        c2 = 0
        for x in nums:
            if var1 != None and x == var1:
                c1 += 1
            if var2 != None and x == var2:
                c2 += 1
        ans = []
        print(var1,count1,var2,count2)
        if c1 > n // 3:
            ans.append(var1)
        if c2 > n // 3 and var1 != var2:
            ans.append(var2)
        return ans
nums =[8,8,7,7,7]
ans = Solution().majorityElement(nums)
print(ans)
