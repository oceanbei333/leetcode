#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for first in range(n-3):
            if first and nums[first] == nums[first-1]:
                continue
            if sum(nums[first:first+4]) > target:
                break
            if sum(nums[first:first+1]+nums[n-3:n]) < target:
                continue
            for second in range(first+1, n-2):
                if second > first+1 and nums[second] == nums[second-1]:
                    continue
                if sum(nums[first:first+1]+ nums[second:second+3]) > target:
                    break
                if nums[first]+nums[second]+ sum(nums[n-2:n]) < target:
                    continue

                third, fourth = second +1, n-1
                while third < fourth:
                    sum_ = nums[first]+nums[second]+nums[third]+nums[fourth]
                    if sum_ == target:
                        res.append([nums[first], nums[second], nums[third], nums[fourth]])
                        while third < fourth and nums[third]== nums[third+1]:
                            third += 1
                        while third < fourth and nums[fourth]== nums[fourth-1]:
                            fourth -= 1
                        third += 1
                        fourth -= 1
                    elif sum_ < target:
                        third += 1
                    else:
                        fourth -= 1
        return res


# @lc code=end

