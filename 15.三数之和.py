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
        res = []
        for i in range(len(nums)-2):
            if i and nums[i] == nums[i-1]:
                continue
            if nums[i] >0:
                break
            for j in range(i+1, len(nums)-1):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + nums[j] >0:
                    break
                for k in range(j+1, len(nums)):
                    if nums[k]<0:
                        continue
                    if k > j+1 and nums[k] == nums[k-1]:
                        continue
                    if not (nums[i]+nums[j]+nums[k]):
                        res.append([nums[i], nums[j], nums[k]])
                    elif nums[i] + nums[j]+nums[k] >0:
                        break
        return res
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i and nums[i] == nums[i-1]:
                continue
            if nums[i] >0:
                break
            aset = set()
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                target = 0 -nums[i] - nums[j]
                if target in aset:
                    res.append([nums[i], target, nums[j]])
                else:
                    aset.add(nums[j])

        return res
        






# @lc code=end

