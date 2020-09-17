class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t: int) -> bool:
        array =[[nums[i],i] for i in range(len(nums))]
        array.sort()
        print(array)
        i=0;j=0
        while i<len(nums):
            while j<len(nums) and i<len(nums) and abs(array[i][0]-array[j][0])<=t:
                print(i,j)
                if abs(array[i][1]-array[j][1])<=k and i!=j:
                    return True
                if j<len(nums):
                    j+=1
                else:
                    i+=1
            i+=1
        return False
nums=[1,2,1,1]
k=1
t=0
ans = Solution().containsNearbyAlmostDuplicate(nums,k,t)
print(ans)