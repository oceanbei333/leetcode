#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        count = 1
        cur = 1
        for index in range(len(nums)-1):
            if nums[index] < nums[index+1]:
                cur = cur+1
            else:
                count = max(cur, count)
                cur = 1
        return max(cur, count)

# @lc code=end
