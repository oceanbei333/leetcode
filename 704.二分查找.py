#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid -1
        return -1
    def search(self, nums: List[int], target: int) -> int:
        from bisect import bisect_left
        index = bisect_left(nums, target)
        return index if index != len(nums) and nums[index] == target else -1

        
# @lc code=end

