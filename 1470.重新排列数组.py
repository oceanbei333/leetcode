#
# @lc app=leetcode.cn id=1470 lang=python3
#
# [1470] 重新排列数组
#

# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        alist = [None]* len(nums)
        for index in range(0, len(nums),2):
            alist[index], alist[index+1] = nums[index//2], nums[index//2+len(nums)//2]
        return alist
# @lc code=end

