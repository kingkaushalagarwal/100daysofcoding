#binary Search
from typing import List
class Solution:
    def binarySearch(self, l, r, arr, val):
        if l <= r:
            mid = (l + r) // 2
            if arr[mid] == val:
                return mid
            elif arr[mid] > val:
                return self.binarySearch(l, mid - 1, arr, val)
            elif arr[mid] < val:
                return self.binarySearch(mid + 1, r, arr, val)
        return -1

    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(0, len(nums) - 1, nums, target)