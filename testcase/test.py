class Solution:
    def findDuplicates(self, nums) :
        ans =[]
        print(len(nums))
        for i in range(len(nums)):
            ind = abs(nums[i])-1
            nums[ind] = nums[ind]*-1
            if nums[ind]>0:
                ans.append(abs(nums[i]))
        return ans
A =[4,3,2,7,8,2,3,1]
ans = Solution().findDuplicates(A)
print(ans)