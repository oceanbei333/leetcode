#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = list()
        for first in range(len(nums)-2):
            if nums[first] > 0:
                return res
            # 去重
            if first and nums[first] == nums[first-1]:
                continue
            second = first+1
            third = len(nums)-1
            while second < third:
                sum_ = nums[first]+nums[second]+nums[third]
                if sum_ > 0:
                    third -= 1
                elif sum_ < 0:
                    second += 1
                else:
                    res.append([nums[first], nums[second], nums[third]])
                    # 去重
                    while second < third and nums[second] == nums[second+1]:
                        second += 1
                    while second < third and nums[third] == nums[third-1]:
                        third -= 1
                    third -= 1
                    second += 1
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = list()
        for first in range(len(nums)-2):
            # 去重
            if first and nums[first] == nums[first-1]:
                continue
            second = first+1
            third = len(nums)-1
            while second < third:
                sum_ = nums[first]+nums[second]+nums[third]
                if sum_ > 0:
                    third -= 1
                elif sum_ < 0:
                    second += 1
                else:
                    res.append([nums[first], nums[second], nums[third]])
                    # 去重
                    while second < third and nums[second] == nums[second+1]:
                        second += 1
                    while second < third and nums[third] == nums[third-1]:
                        third -= 1
                    third -= 1
                    second += 1
        return res

# @lc code=end
